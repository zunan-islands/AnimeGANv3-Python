
# AnimeGANv3-Python

A command-line tool that transforms photos into an anime look using ONNX Runtime trained models of [AnimeGANv3](https://github.com/TachibanaYoshino/AnimeGANv3).  
Based on the inference process of [AnimeGANv3.exe](https://github.com/TachibanaYoshino/AnimeGANv3/blob/master/AnimeGANv3/AnimeGANv3.exe).

## Install

It is written in Python, so it is cross-platform.  
However, it consumes a large amount of CPU and memory because inference is performed on the CPU.

Requirements: Python 3.10 / pip / pipenv

```bash
# clone code
git clone https://github.com/tsukumijima/AnimeGANv3-Python.git
cd AnimeGANv3-Python

# install pipenv
pip install pipenv

# run pipenv sync
## Windows (PowerShell)
$env:PIPENV_VENV_IN_PROJECT="true"; pipenv sync
## Linux
PIPENV_VENV_IN_PROJECT="true" pipenv sync
```

## Usage

```bash
# run AnimeGANv3-Python.py inside pipenv
pipenv run python AnimeGANv3-Python.py C:/path/to/input_images C:/path/to/output_images --onnx-model-type H40
```

```
usage: AnimeGANv3-Python.py [-h] [--onnx-model-type {H40,H50,H64}] InputDirPath OutputDirPath

positional arguments:
  InputDirPath          Image directory path of input source
  OutputDirPath         Image directory path of output destination

options:
  -h, --help            show this help message and exit
  --onnx-model-type {H40,H50,H64}
                        onnx model type (H40, H50, H64)
```

## Examples

⬅ original photo | transform into anime look ➡

![example_01](https://user-images.githubusercontent.com/39271166/191425491-2900b532-e5b4-497a-9b3c-d539fdec8469.jpg)
![example_02](https://user-images.githubusercontent.com/39271166/191425500-726c1691-7b84-4e1b-8f06-9ce60cddb7c4.jpg)
![example_03](https://user-images.githubusercontent.com/39271166/191425514-179d30f9-adc8-4c33-a8e1-cf590ffb08ff.jpg)
![example_04](https://user-images.githubusercontent.com/39271166/191425533-5d530f6f-b19a-419f-9952-86c334540c0f.jpg)
![example_05](https://user-images.githubusercontent.com/39271166/191425459-e6aded57-9eae-4885-8d64-4ad9f471a665.jpg)
![example_06](https://user-images.githubusercontent.com/39271166/191425470-ecab3470-e6c6-4465-8771-37de595f3079.jpg)
![example_07](https://user-images.githubusercontent.com/39271166/191425480-41273edb-1f88-43dd-a32f-1434be0b5234.jpg)
![example_08](https://user-images.githubusercontent.com/39271166/191425483-da3d9d3c-74fc-4e71-8de4-05ec0a51f27e.jpg)

## License

[MIT License](License.txt)
