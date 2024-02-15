# chat10b.py
# chat9.py updated with https://ollama.ai/blog/python-javascript-libraries
# uses a simple list for context. See chat10c.py for more.

import gradio as gr
import csv
import datetime
import ollama

def list_ollama_models():
    """
    Lists locally available ollama models. https://github.com/jmorganca/ollama/blob/main/docs/api.md#list-local-models
    """
    models = ollama.list()
    for model in models['models']:
        print(f"{model['name']}")

list_ollama_models()

context = []

# Ask user for model name
model_name = input("Enter the model to use (e.g., 'codellama' for 'codellama:latest'): ")

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
    Generates a response from an API using the given input, including context. Takes one argument, `input`, which can be any iterable data.

    Args:
    input (Any iterable): The data to be sent as an input to the API.

    Returns:
    The actual response from the API.
    """

    context.append(input)
    appended_input = "\n".join(context)

    response = ollama.chat(model=model_name, messages=[
    {
        'role': 'user',
        'content': appended_input,
    }
    ])

    response = response['message']['content']
    # Save input and output to CSV file
    save_to_csv([input, response])

    return response

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

demo.launch()
