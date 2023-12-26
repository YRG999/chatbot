# chatbot.py note:
# openai.lib._old_api.APIRemovedInV1: 
# You tried to access openai.ChatCompletion, but this is no longer supported in openai>=1.0.0 - see the README at https://github.com/openai/openai-python for the API.
# You can run `openai migrate` to automatically upgrade your codebase to use the 1.0.0 interface. 
# Alternatively, you can pin your installation to the old version, e.g. `pip install openai==0.28`
# A detailed migration guide is available here: https://github.com/openai/openai-python/discussions/742
# ---
# TODO update chat_with_gpt4 function to use new SDK methods.

import os
from openai import OpenAI  # Updated import statement
import csv
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

# Set your API key
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # Updated API key initialization
)

# Initialize the list of messages
messages = []

def compress_text(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            if len(w) > 7:
                w = w[:7] + '..'
            filtered_sentence.append(w)
    return ' '.join(filtered_sentence)

def save_to_csv(role, content, compressed_content):
    with open('_notes/chat_history.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([role, content, compressed_content])

def chat_with_gpt4():
    # Ask the user for input
    user_input = input("You: ")

    # Save the user's input to the CSV and add it to the messages
    compressed_input = compress_text(user_input)
    save_to_csv("user", user_input, compressed_input)

    # Construct the chat history for the prompt
    chat_history = "You are a helpful assistant.\n"
    for message in messages:
        role = message["role"]
        content = message["content"]
        chat_history += f"{role.capitalize()}: {content}\n"

    # Append the latest user input
    chat_history += f"You: {user_input}\n"

    # Get the response from the API
    try:
        response = client.Completion.create(
            model="gpt-4",
            prompt=chat_history,
            max_tokens=150,  # Adjust as needed
            stop=["\n", " You:", " Assistant:"]
        )
        assistant_output = response.choices[0].text.strip()
    except Exception as e:
        print("Error in API call:", e)
        assistant_output = "Sorry, I am unable to respond at the moment."

    # Print the assistant's output
    print("GPT-4: ", assistant_output)

    # Compress the assistant's output, save it to the CSV, and add it to the messages
    compressed_output = compress_text(assistant_output)
    save_to_csv("assistant", assistant_output, compressed_output)
    messages.append({"role": "assistant", "content": assistant_output})

# Example usage
chat_with_gpt4()
