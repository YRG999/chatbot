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
*Requires an [OpenAI API key](https://platform.openai.com/api-keys). See `.env_example` for details.*
* `openaichatbot3.py` - Creates a chatbot using Flask. Saves conversation in session conversation history to file after logout. See previous files and chatbot notes for iterative design history.

## Transformers & llm
* *Uses the Python [transformers](https://pypi.org/project/transformers/) library.*
  * `textclassify.py` - for sentiment analysis.
  * `textcomplete.py` - to completes a sentence.
* `llmtest.py` & `llmtest2.py` - testing [LLM CLI](https://llm.datasette.io).
* `testllamacpp.py` - use `install_llamacpp.sh` to install on Apple Silicon.

## ollama
*Requires [ollama](https://ollama.ai/) and at least one model installed.*
* `chat9.py` - uses ollama to create a local chatbot. 
  * Lists models installed locally. 
  * Asks user to enter the name of the model to use. 
  * Saves input & output to `output-{model_name}.csv`. 
  * Uses ollama `context` parameter for conversation history. 
  * See [ollama_models](doc/ollama_models.md) for examples of models used. 
  * *Inspired by `openchat_context.py`*
* In progress: `chat10.py`, `chat10a.py`, `chat10b.py`

## Utilities
* `createKey.py` - creates a key to use for Flask sessions.
* `filebot/addline` - file to parse GPT bulleted responses prior to saving conversation history.

## Doc
* [ChatGPT notes](doc/ChatGPTnotes.md)
* [Programming notes](doc/Programmingnotes.md)
* [Ollama resources](doc/ollama_res.md)
* [Ollama models](doc/ollama_models.md)
* [Chatbot_notes1](doc/Chatbot_notes1.md)
* [Chatbot_notes2](doc/Chatbot_notes2.md)
