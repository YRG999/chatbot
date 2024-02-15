# ollama resources
* Adapted from [Ollama Is INSANE: Building Open-Source ChatGPT From Scratch (FULLY Local Tutorial)](https://www.youtube.com/watch?v=rIRkxZSn-A8) by Matthew Berman
  * [Github repo](https://gist.github.com/mberman84/a1291cfb08d0a37c3d439028f3bc5f26)
  * Uses [gradio](https://www.gradio.app/main/guides/installing-gradio-in-a-virtual-environment)

# links
* [leaderboard](https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard)
* [chatbot arena](https://chat.lmsys.org/?arena)
* [ollama.ai](https://ollama.ai/) | [Github](https://github.com/jmorganca/ollama)
* [lmstudio.ai](https://lmstudio.ai/) - did not try this yet

## definitions
* [What is quantization?](https://deci.ai/quantization-and-quantization-aware-training/#:~:text=Quantization%20is%20a%20common%20technique,rather%20than%20after%20the%20fact.)
* [FLAN](https://blog.research.google/2021/10/introducing-flan-more-generalizable.html)
* [ollama models](ollama_models.md)

## more ollama doc
* had to figure out what the response value was for the generate method. Found out it's response, so used response['response'] to get it.
* https://github.com/ollama/ollama-python?tab=readme-ov-file
* https://github.com/ollama/ollama/blob/main/docs/api.md
* https://github.com/ollama/ollama/blob/main/docs/modelfile.md#valid-parameters-and-values
* https://github.com/ollama/ollama/blob/main/docs/modelfile.md#system