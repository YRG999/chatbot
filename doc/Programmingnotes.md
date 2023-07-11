# Programming notes

- [Programming notes](#programming-notes)
  - [pip list](#pip-list)
  - [Available pipeline tasks](#available-pipeline-tasks)
  - [Add pytorch to requirements.txt](#add-pytorch-to-requirementstxt)

## pip list

Install requirements and the following will be installed.

```
Package                 Version
----------------------- --------
absl-py                 1.4.0
aiohttp                 3.8.4
aiosignal               1.3.1
astunparse              1.6.3
async-timeout           4.0.2
attrs                   23.1.0
cachetools              5.3.1
certifi                 2023.5.7
charset-normalizer      3.2.0
click                   8.1.4
filelock                3.12.2
flatbuffers             23.5.26
frozenlist              1.3.3
fsspec                  2023.6.0
gast                    0.4.0
google-auth             2.21.0
google-auth-oauthlib    1.0.0
google-pasta            0.2.0
grpcio                  1.56.0
h5py                    3.9.0
huggingface-hub         0.16.4
idna                    3.4
Jinja2                  3.1.2
joblib                  1.3.1
keras                   2.13.1
libclang                16.0.0
Markdown                3.4.3
MarkupSafe              2.1.3
mpmath                  1.3.0
multidict               6.0.4
mypy-extensions         1.0.0
networkx                3.1
nltk                    3.8.1
numpy                   1.24.3
oauthlib                3.2.2
openai                  0.27.8
opt-einsum              3.3.0
packaging               23.1
Pillow                  10.0.0
pip                     23.1.2
protobuf                4.23.4
pyasn1                  0.5.0
pyasn1-modules          0.3.0
pyre-extensions         0.0.29
PyYAML                  6.0
regex                   2023.6.3
requests                2.31.0
requests-oauthlib       1.3.1
rsa                     4.9
safetensors             0.3.1
setuptools              58.1.0
six                     1.16.0
sympy                   1.12
tensorboard             2.13.0
tensorboard-data-server 0.7.1
tensorflow              2.13.0
tensorflow-estimator    2.13.0
tensorflow-macos        2.13.0
termcolor               2.3.0
tokenizers              0.13.3
torch                   2.0.1
torchvision             0.15.2
tqdm                    4.65.0
transformers            4.30.2
typing_extensions       4.5.0
typing-inspect          0.9.0
urllib3                 1.26.16
Werkzeug                2.3.6
wheel                   0.40.0
wrapt                   1.15.0
xformers                0.0.20
yarl                    1.9.2
```

[back](README.md)

## Available pipeline tasks

```
available tasks are ['audio-classification', 'automatic-speech-recognition', 'conversational', 'depth-estimation', 'document-question-answering', 'feature-extraction', 'fill-mask', 'image-classification', 'image-segmentation', 'image-to-text', 'mask-generation', 'ner', 'object-detection', 'question-answering', 'sentiment-analysis', 'summarization', 'table-question-answering', 'text-classification', 'text-generation', 'text2text-generation', 'token-classification', 'translation', 'video-classification', 'visual-question-answering', 'vqa', 'zero-shot-audio-classification', 'zero-shot-classification', 'zero-shot-image-classification', 'zero-shot-object-detection', 'translation_XX_to_YY']"
```

## Add pytorch to requirements.txt
* https://stackoverflow.com/questions/60912744/install-pytorch-from-requirements-txt
* *Ended up just adding `torch` and `torchvision` on separate lines in `requirements.txt`.*