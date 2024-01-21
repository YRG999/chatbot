# openaichatbot
# Chat with GPT model; no history.

import os
from flask import Flask, request, render_template
from openai import OpenAI

app = Flask(__name__)

# Instantiate the OpenAI client
# client = OpenAI(api_key='your-api-key-here')  # Replace with your actual API key
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],
)

@app.route('/', methods=['GET', 'POST'])
def chat():
    user_input = ''
    bot_response = ''
    if request.method == 'POST':
        user_input = request.form['user_input']
        bot_response = get_response(user_input)
    return render_template('chat.html', user_input=user_input, bot_response=bot_response)

def get_response(user_input):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_input},
                {"role": "assistant", "content": ""}  # Assistant's response will be generated here
            ],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        # Access the response as an attribute
        return response.choices[0].message.content
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
