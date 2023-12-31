# chat9.py
# Updated conversation history by using ollama's context parameter
# https://github.com/jmorganca/ollama/blob/main/docs/api.md#generate-a-completion

import requests
import json
import gradio as gr
import csv
import datetime

def list_ollama_models():
    """
    Lists locally available ollama models. https://github.com/jmorganca/ollama/blob/main/docs/api.md#list-local-models
    """
    url = "http://localhost:11434/api/tags"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        models = data["models"]
        for model in models:
            print(model["name"])
        # print(models)
    else:
        print("Error:", response.status_code, response.text)

list_ollama_models()

# Ask user for model name
model_name = input("Enter the model to use (e.g., 'codellama' for 'codellama:latest'): ")

url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json',
}

context = []

def save_to_csv(input_output):
    """
    Saves the given input-output data as rows in a CSV file named 'output-{model_name}.csv'. Takes one argument `input_output`, which can be either an iterable (like a single list) or an iterable of iterables (like a list containing multiple sub-lists).

    Args:
    input_output (Iterable or Iterable of Iterables): The data to be saved in the CSV file.
    """
    with open('output-%s.csv' % model_name, mode='a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        row_data = ["---", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), *input_output]
        writer.writerow(row_data)

def generate_response(input):
    """
    Generates a response from an API using the given input and saves the input and output to a CSV file. Takes one argument, `input`, which can be any iterable data.

    Args:
    input (Any iterable): The data to be sent as an input to the API.

    Returns:
    The actual response from the API if it returns a status code 200 (success). Otherwise, it prints an error message and returns None.
    """

    global context

    data = {
        "model": model_name,
        "stream": False,
        "prompt": input,
        "context": context
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        context = data["context"]

        # Save input and output to CSV file
        save_to_csv([input, actual_response])

        return actual_response
    else:
        print("Error:", response.status_code, response.text)
        return None

def clear_history():
    """
    Clears conversation history.
    """
    global context
    context = []
    return None

with gr.Blocks() as demo:
    with gr.Row():
        input_text = gr.Textbox(placeholder="Enter your prompt here...")
        generate_button = gr.Button("Generate Response")
        clear_button = gr.Button("Clear History")
    output_text = gr.Textbox()

    input_text.submit(generate_response, inputs=input_text, outputs=output_text)
    generate_button.click(generate_response, inputs=input_text, outputs=output_text)
    clear_button.click(clear_history, inputs=None, outputs=output_text)
    # TODO: create clear textbox button

demo.launch()
