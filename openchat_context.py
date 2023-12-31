# openchat_context.py
# Adapted from [Ollama Is INSANE: Building Open-Source ChatGPT From Scratch (FULLY Local Tutorial)](https://www.youtube.com/watch?v=rIRkxZSn-A8) by Matthew Berman
# Original code: https://gist.github.com/mberman84/a1291cfb08d0a37c3d439028f3bc5f26
# Uses [gradio](https://www.gradio.app/main/guides/installing-gradio-in-a-virtual-environment)

import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json',
}

# conversation_history = []
context = []

def generate_response(prompt):
    # conversation_history.append(prompt)

    # full_prompt = "\n".join(conversation_history)
    global context

    data = {
        "model": "mistral",
        "stream": False,
        # "prompt": full_prompt,
        "prompt": prompt,
        "context": context
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        # conversation_history.append(actual_response)
        context = data["context"]
        return actual_response
    else:
        print("Error:", response.status_code, response.text)
        return None

iface = gr.Interface(
    fn=generate_response,
    # inputs=gr.inputs.Textbox(lines=2, placeholder="Enter your prompt here..."),
    inputs=gr.Textbox(lines=2, placeholder="Enter your prompt here..."),
    outputs="text"
)

iface.launch()