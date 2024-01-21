# openaichatbot2.py
# Chat with GPT model with history; no saving history or clearing session.

import os
from flask import Flask, request, render_template, session
from openai import OpenAI
from flask_session import Session

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY', 'default-secret-key')
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'],)

@app.route('/', methods=['GET', 'POST'])
def chat():
    if 'conversation' not in session:
        session['conversation'] = []

    if request.method == 'POST':
        user_input = request.form['user_input']

        # Get the bot's response
        bot_response = get_response(user_input)

        # Append the user's message and the bot's response once
        session['conversation'].append({"role": "user", "content": user_input})
        session['conversation'].append({"role": "assistant", "content": bot_response})
        session.modified = True  # Mark the session as modified

    return render_template('chat2.html', conversation=session['conversation'])

def get_response(user_input):
    try:
        # Make the API call using the current conversation history
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=session['conversation'] + [{"role": "user", "content": user_input}],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        # Retrieve the bot's response
        bot_response = response.choices[0].message.content

        return bot_response
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
