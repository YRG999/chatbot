# Hugging Face notes <!-- omit in toc -->

- [ChatGPT-4](#chatgpt-4)
  - [Explain hugging face](#explain-hugging-face)
  - [I got a runtime error](#i-got-a-runtime-error)
  - [No model was supplied](#no-model-was-supplied)
- [pip list](#pip-list)
- [Available tasks](#available-tasks)
- [More ChatGPT-4](#more-chatgpt-4)
  - [What do these console messages mean?](#what-do-these-console-messages-mean)
  - [Should I install Pytorch?](#should-i-install-pytorch)

# ChatGPT-4
*Tue, Jul 11, 2023* | [back](README.md)

## Explain hugging face
Explain how to use hugging face using working samples in python.

---

Hugging Face's Transformers is a popular Python library for Natural Language Processing (NLP) tasks, which provides state-of-the-art models like BERT, GPT-2, and T5. It's used for tasks such as text classification, named entity recognition, text generation, and more.

For this explanation, let's consider a couple of examples: text classification and text generation.

Note: These examples require the Transformers library to be installed, and also require an internet connection to download the model weights. As this environment doesn't have internet access, I will provide the code snippets without running them.

### Text Classification
In text classification, we are given a piece of text and we want to categorize it into one or more classes. For instance, we might want to classify movie reviews as positive or negative.

Let's use the BERT model for this task:

```python
from transformers import pipeline

# Initialize the classifier
classifier = pipeline("sentiment-analysis")

# Use the model to classify a piece of text
result = classifier("I love this movie!")[0]

# Output the classification results
print(f"label: {result['label']}, with score: {result['score']}")
```

When you run this code, it will output something like:

```vbnet
label: POSITIVE, with score: 0.9998
```

### Text Generation
In text generation, we want to generate new text based on some input. For instance, we might want to generate a continuation of a given text.

Let's use the GPT-2 model for this task:

```python
from transformers import pipeline

# Initialize the text generator
generator = pipeline("text-generation")

# Use the model to generate a continuation of the given text
result = generator("In a world where")[0]

# Output the generated text
print(result['generated_text'])
```

When you run this code, it will output a generated text that continues the given input. The output will be different every time you run it, as GPT-2 includes randomness in its text generation.

Please note that you need to install the Transformers library before you can use it. You can install it via pip:

```shell
pip install transformers
```

Also, these examples use the pipeline API provided by the Transformers library, which is a high-level API that abstracts away many details. If you need more control over the process, you can use the lower-level APIs provided by the library.

## I got a runtime error
I got a runtime error: RuntimeError: At least one of TensorFlow 2.0 or PyTorch should be installed. To install TensorFlow 2.0, read the instructions at https://www.tensorflow.org/install/ To install PyTorch, read the instructions at https://pytorch.org/.

---

The Hugging Face Transformers library requires either TensorFlow or PyTorch to be installed in order to work. These are two popular deep learning libraries that Transformers uses to run the machine learning models.

The error message you're seeing suggests that neither of these libraries is currently installed in your environment.

Here's how to install them:

TensorFlow: You can install TensorFlow via pip using the following command:
```bash
pip install tensorflow
```

Or if you want to install the GPU version of TensorFlow (which can significantly speed up computations if you have a compatible GPU), use this command instead:

```bash
pip install tensorflow-gpu
```

PyTorch: The command to install PyTorch depends on your system configuration. You can get the appropriate command from the PyTorch website by selecting your configuration and then copying the command it provides. It should look something like this:

```bash
pip install torch torchvision
```

After installing one or both of these libraries, you should be able to use the Transformers library without seeing the error message.

Remember, the above instructions require an internet connection to download and install the packages. If you're running in a closed environment or behind a firewall, you'll need to follow your organization's procedures for installing Python packages.

## No model was supplied
It worked, but I got the following message: No model was supplied, defaulted to distilbert-base-uncased-finetuned-sst-2-english and revision af0f99b (https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english).
Using a pipeline without specifying a model name and revision in production is not recommended.

Can you explain this?

---

Absolutely! The warning message you're seeing is due to the fact that you didn't explicitly specify a model when you created the pipeline.

When you call pipeline("sentiment-analysis") or pipeline("text-generation"), the Hugging Face Transformers library defaults to using a pre-trained model that it deems suitable for the task. In this case, for the sentiment analysis task, it's using distilbert-base-uncased-finetuned-sst-2-english, which is a version of the DistilBERT model that has been fine-tuned on a sentiment analysis dataset (SST-2).

While this behavior is convenient for getting started quickly and experimenting, it's generally not recommended for production use. This is because the default model can change over time as the library is updated, which could lead to unexpected changes in your application's behavior.

To have more control and stability, you should explicitly specify the model you want to use when creating the pipeline. For example, if you want to continue using the same model, you can do:

```python
from transformers import pipeline

# Initialize the classifier with a specific model
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Use the model to classify a piece of text
result = classifier("I love this movie!")[0]

# Output the classification results
print(f"label: {result['label']}, with score: {result['score']}")
This way, even if the Transformers library is updated in the future, your code will continue to use the same model and behave the same way.
```

*ChatGPT may produce inaccurate information about people, places, or facts. ChatGPT May 24 Version*

[back](README.md)

# pip list

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

# Available tasks

```
available tasks are ['audio-classification', 'automatic-speech-recognition', 'conversational', 'depth-estimation', 'document-question-answering', 'feature-extraction', 'fill-mask', 'image-classification', 'image-segmentation', 'image-to-text', 'mask-generation', 'ner', 'object-detection', 'question-answering', 'sentiment-analysis', 'summarization', 'table-question-answering', 'text-classification', 'text-generation', 'text2text-generation', 'token-classification', 'translation', 'video-classification', 'visual-question-answering', 'vqa', 'zero-shot-audio-classification', 'zero-shot-classification', 'zero-shot-image-classification', 'zero-shot-object-detection', 'translation_XX_to_YY']"
```

# More ChatGPT-4

## What do these console messages mean?
All PyTorch model weights were used when initializing TFGPT2LMHeadModel.

All the weights of TFGPT2LMHeadModel were initialized from the PyTorch model.
If your task is similar to the task the model of the checkpoint was trained on, you can already use TFGPT2LMHeadModel for predictions without further training.
Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.

UserWarning: Using `max_length`'s default (50) to control the generation length. This behaviour is deprecated and will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.

---

These console messages provide information about how the model was loaded, initialized, and set up for prediction. Here's what each of them mean:

1. **"All PyTorch model weights were used when initializing TFGPT2LMHeadModel."**: This message indicates that the weights of the PyTorch model were successfully used to initialize the TensorFlow version of the GPT-2 model (`TFGPT2LMHeadModel`). This is generally done when you load a model that was trained using PyTorch, but you want to use it in TensorFlow.

2. **"All the weights of TFGPT2LMHeadModel were initialized from the PyTorch model."**: This message reinforces the previous message, stating that all the weights of the TensorFlow model have been correctly initialized from the corresponding PyTorch model.

3. **"If your task is similar to the task the model of the checkpoint was trained on, you can already use TFGPT2LMHeadModel for predictions without further training."**: This means that if the task you're using the model for is similar to the task the model was originally trained on, you can use the model to make predictions without needing to train it further. This is the beauty of transfer learning: models that are pre-trained on one task can often be used with little to no additional training on a related task.

4. **"Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation."**: For the GPT-2 model, the end-of-sentence token (`eos_token_id`) is being used as the padding token (`pad_token_id`). This is done because GPT-2 doesn't have a specific padding token, and it's necessary to have one for certain processing steps. The specific value 50256 is the token ID of the end-of-sentence token in the GPT-2 model's vocabulary.

5. **"UserWarning: Using `max_length`'s default (50) to control the generation length. This behaviour is deprecated and will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation."**: This is a warning that the default behavior of using `max_length` to control the length of the generated text is deprecated and will be removed in a future version of the Transformers library. Instead, it's recommended to use the `max_new_tokens` parameter. So, if you were generating text with something like `generator("In a world where", max_length=100)`, you should change it to `generator("In a world where", max_new_tokens=100)`.

These messages are largely informational and don't indicate any problems with your code or the model. However, you should heed the deprecation warning and update your code to use `max_new_tokens` instead of `max_length` if you're using the latter.

## Should I install Pytorch?

If you're already using Hugging Face's Transformers library with TensorFlow and it's serving your purposes, you may not need to install PyTorch. Both TensorFlow and PyTorch are powerful deep learning libraries, and Transformers can use either one.

However, there are reasons you might want to consider installing PyTorch:

- **Some models only support PyTorch**: While many models in the Transformers library support both TensorFlow and PyTorch, some only support PyTorch. If you want to use one of these PyTorch-only models, you'll need to install PyTorch.

- **Easier debugging and development**: Some people find PyTorch easier to debug and develop with because its dynamic computation graph allows for more flexibility and it's more pythonic in nature. 

- **Tutorials and examples**: A significant portion of tutorials, guides, and examples related to Hugging Face Transformers and deep learning, in general, are written in PyTorch. So, having PyTorch installed can be useful for learning and experimenting.

To install PyTorch, you can use the appropriate command from the PyTorch website, which depends on your system and package manager. For pip, it might look something like this:

```bash
pip install torch torchvision
```

Remember to follow the instructions specific to your operating system and Python environment from the [official PyTorch website](https://pytorch.org/).

# Add pytorch to requirements.txt
* https://stackoverflow.com/questions/60912744/install-pytorch-from-requirements-txt
* *Ended up just adding `torch` and `torchvision` on separate lines in `requirements.txt`.*
