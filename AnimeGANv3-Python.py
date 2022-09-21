
import argparse
import cv2
import onnxruntime
import numpy as np
import sys
import time
from pathlib import Path
from numpy import floating
from numpy.typing import NDArray
from typing import Any, Literal


def LoadImageAsNDArray(path: Path) -> tuple[NDArray[floating[Any]], tuple[int, int]]:
    image_mat = cv2.imread(str(path))
    image, width_and_height = PreprocessImage(image_mat)
    image = np.asarray(np.expand_dims(image, 0))
    return (image, tuple(width_and_height))

def PreprocessImage(image: np.ndarray[int, np.dtype[np.generic]], x32=True) -> tuple[NDArray[floating[Any]], list[int]]:
    height, width = image.shape[:2]
    if x32:
        def to_32s(x):
            if x < 256:
                return 256
            return x - x % 32
        image = cv2.resize(image, (to_32s(width), to_32s(height)))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB).astype(np.float32) / 127.5 - 1.0
    return (image, [width, height])

def SaveImage(transform_image_ndarray: NDArray, width_and_height: tuple[int, int], output_image_path: Path) -> None:
    transform_image_ndarray = (transform_image_ndarray.squeeze() + 1.0) / 2 * 255
    transform_image_ndarray = transform_image_ndarray.astype(np.uint8)
    transform_image_ndarray = cv2.resize(transform_image_ndarray, (width_and_height[0], width_and_height[1]))
    cv2.imwrite(str(output_image_path), cv2.cvtColor(transform_image_ndarray, cv2.COLOR_RGB2BGR))

def TransformImage(input_dir_path: Path, output_dir_path: Path, onnx_model_type: Literal['H40', 'H50', 'H64']) -> None:

    # get input image paths
    input_image_paths = [i for i in Path(input_dir_path).glob('**/*.*') if i.suffix.lower() in ('.jpg', '.jpeg', '.png')]
    if len(input_image_paths) == 0:
        print('Error: No images in ".jpg, ".jpeg", ".png" format in specified directory.')
        sys.exit(1)

    # create output dir
    output_dir_path.mkdir(parents=True, exist_ok=True)

    # load onnx runtime model
    print('Loading ONNX runtime model...')
    onnx_path = Path(__file__).resolve().parent / f'models/animeganv3_{onnx_model_type}_model.onnx'
    with open(onnx_path, mode='rb') as fp:
        onnx = fp.read()
    session = onnxruntime.InferenceSession(onnx, providers=['CPUExecutionProvider'])
    x = session.get_inputs()[0].name
    y = session.get_outputs()[0].name
    print('Loaded ONNX runtime model.')

    # start inference
    print('Processing...')
    total_start_at = time.time()
    for input_image_path in input_image_paths:
        start_at = time.time()

        # load image as ndarray
        image_ndarray, width_and_height = LoadImageAsNDArray(input_image_path)

        # run inference
        transform_data = session.run(None, {x: image_ndarray})

        # save image
        output_image_path = output_dir_path / input_image_path.name
        SaveImage(transform_data[0], width_and_height, output_image_path)
        print(f'Processed image: "{input_image_path}" ({width_and_height[0]}×{width_and_height[1]}) time: {time.time() - start_at:.3f}s')

    total_end_at = time.time()
    print(f"Average time per image: {(total_end_at - total_start_at) / len(input_image_paths):.3f}s")


if __name__ == '__main__':

    # parse arguments
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('InputDirPath', help='Image directory path of input source')
    parser.add_argument('OutputDirPath', help='Image directory path of output destination')
    parser.add_argument('--onnx-model-type', choices=('H40', 'H50', 'H64'), default='H40', help='onnx model type (H40, H50, H64)')
    args = parser.parse_args()

    input_dir_path: Path = Path(args.InputDirPath)
    output_dir_path: Path = Path(args.OutputDirPath)
    onnx_model_type: Literal['H40', 'H50', 'H64'] = args.onnx_model_type

    # start transform
    TransformImage(input_dir_path, output_dir_path, onnx_model_type)
