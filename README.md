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
* `chatbot.py` - uses OpenAI and `nltk` to create a chatbot.

## Transformers
* The following use the Python [transformers](https://pypi.org/project/transformers/) library:
* `textclassify.py` - for sentiment analysis.
* `textcomplete.py` - to completes a sentence.

## ollama
* `openchat5.py` - uses ollama to create a local chatbot. Saves input & output to `output.csv`. Uses simplistic text history for context.
* **Requirement: Install [ollama](https://ollama.ai/) and latest [mistral](https://ollama.ai/library/mistral) LLM.**

## Doc
* [ChatGPT notes](doc/ChatGPTnotes.md)
* [Programming notes](doc/Programmingnotes.md)
* [ollama resources](doc/ollama_res.md)
