import os
import openai
import csv
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

# Set your API key
openai.api_key = os.getenv("OPENAI_API_KEY")

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
    messages.append({"role": "system", "content": "You are a helpful assistant."})
    messages.append({"role": "user", "content": user_input})

    # Get the response from the API
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )

    # Print the assistant's output
    print("GPT-4: ", response['choices'][0]['message']['content'])

    # Compress the assistant's output, save it to the CSV, and add it to the messages
    compressed_output = compress_text(response['choices'][0]['message']['content'])
    save_to_csv("assistant", response['choices'][0]['message']['content'], compressed_output)
    messages.append({"role": "assistant", "content": response['choices'][0]['message']['content']})

# Example usage
chat_with_gpt4()
