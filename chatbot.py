import openai
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

# Set your API key
openai.api_key = 'your-api-key'

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

def chat_with_gpt4(user_input):
    # Compress the user's input and add it to the messages
    compressed_input = compress_text(user_input)
    messages.append({"role": "system", "content": "You are a helpful assistant."})
    messages.append({"role": "user", "content": compressed_input})

    # Get the response from the API
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )

    # Compress the assistant's output and add it to the messages
    compressed_output = compress_text(response['choices'][0]['message']['content'])
    messages.append({"role": "assistant", "content": compressed_output})

    # Return the assistant's output
    return response['choices'][0]['message']['content']

# Example usage
print(chat_with_gpt4("Hello, how are you?"))
