# chat6.py
# Update to openchat5.py
# Asks for a model name and uses it in the generate_response function to generate responses from the API and the save_to_csv function to save to a CSV with the model name appended.

import requests
import json
import gradio as gr
import csv
import datetime

# Ask user for model name
model_name = input("Enter the name of the model you want to use (e.g., 'codellama'): ")

url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json',
}

conversation_history = []

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
    conversation_history.append(input)

    full_prompt = "\n".join(conversation_history)

    data = {
        "model": model_name,
        "stream": False,
        "prompt": full_prompt,
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        conversation_history.append(actual_response)

        # Save input and output to CSV file
        save_to_csv([input, actual_response])

        return actual_response
    else:
        print("Error:", response.status_code, response.text)
        return None

iface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(placeholder="Enter your prompt here..."),
    outputs="text"
)

iface.launch()
