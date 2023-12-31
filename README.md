# Chatbot

Programs to create local chatbots\*.

*\*Except for the first one that uses OpenAI.*

## Set up
Create & activate new virtual environment

   ```bash
   $ python3 -m venv venv
   $ . venv/bin/activate
   ```

Install the requirements

   ```bash
   $ pip install -r requirements.txt
   ```

## OpenAI (not local)
*Requires an [OpenAI API key](https://platform.openai.com/api-keys).*
* `chatbot.py` - uses OpenAI and `nltk` to create a chatbot. Deprecated, uses old openai SDK.
* `chatbot2.py` - needs to be updated to use new openai SDK.

## Transformers
*Uses the Python [transformers](https://pypi.org/project/transformers/) library.*
* `textclassify.py` - for sentiment analysis.
* `textcomplete.py` - to completes a sentence.

## ollama
*Requires [ollama](https://ollama.ai/) and at least one model installed.*
* `chat9.py` - uses ollama to create a local chatbot. Lists models installed locally. Asks user to enter the name of the model to use. Saves input & output to `output-{model_name}.csv`. Uses ollama `context` parameter for conversation history.

## Doc
* [ChatGPT notes](doc/ChatGPTnotes.md)
* [Programming notes](doc/Programmingnotes.md)
* [ollama resources](doc/ollama_res.md)
