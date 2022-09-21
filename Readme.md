
# AnimeGANv3-Python

A tool that transforms photos into an anime look using ONNX Runtime trained models of [AnimeGANv3](https://github.com/TachibanaYoshino/AnimeGANv3).  
Based on the inference process of AnimeGANv3.exe.

## Install

Requirements: Python 3.10 / pip / pipenv

```bash
# clone code
git clone https://github.com/tsukumijima/AnimeGANv3-Python.git
cd AnimeGANv3-Python

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

## License

[MIT License](License.txt)
