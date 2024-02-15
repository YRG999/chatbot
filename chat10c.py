# latest chatbot

# uses https://ollama.ai/blog/python-javascript-libraries
# integrated answer from https://github.com/ollama/ollama-python/issues/38
    # The response from a generate call will return a context object. To continue the conversation, you can pass this directly into the next call:
    # r1 = ollama.generate(model='llama2', prompt='hi!')
    # r2 = ollama.generate(model='llama2', prompt='hi again!', context=r1['context'])
    # Context is the token representations of the inputs and outputs up to and including the response
# changed ollama.chat to ollama.generate
    # https://github.com/ollama/ollama-python/issues/21
    # ollama.generate calls ollama's generate endpoint which is intended for text or code completion but can also be used for chat. it takes prompt, template, and system as its main input fields.
    # ollama.chat calls ollama's chat endpoint which is specialized for chat interactions. it takes messages as its main input field

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

# Function to make a call to ollama and update the context
def generate_response(prompt):
    global context  # Ensure we're updating the global context variable
    if context is None:
        response = ollama.generate(model=model_name, prompt=prompt)
    else:
        response = ollama.generate(model=model_name, prompt=prompt, context=context)
    
    # Update the context with the new one returned by the call
    context = response['context']

    save_to_csv([prompt, response['response']])
    
    return response['response']

def clear_history():
    """
    Clears conversation history.
    """
    global context
    context = None

def main():
    # Initialize the context variable; this may not be necessary depending on how ollama handles it.
    global context
    context = None

    list_ollama_models()

    # Ask user for model name
    global model_name
    model_name = input("Enter the model to use (e.g., 'codellama' for 'codellama:latest'): ")

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

if __name__ == "__main__":
    main()
