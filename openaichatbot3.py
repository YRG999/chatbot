# openaichatbot3.py
# Chat with GPT model with history with the ability to save and clear history.
# Appends datetime to file and CSV.

import os
from flask import Flask, request, render_template, session, make_response
from openai import OpenAI
from flask_session import Session
import csv
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY', 'default-secret-key')
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'],)

def save_conversation_to_file():
    closing_line = "End of Conversation"
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")  # Format: 'YYYYMMDD_HHMMSS'
    filename = f'conversation_history_{current_time}.csv'

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Role', 'Content', 'Timestamp'])
        for message in session.get('conversation', []):
            timestamp = message.get('timestamp', '')  # Assuming each message has a 'timestamp'
            writer.writerow([message['role'], message['content'], timestamp])
        writer.writerow([closing_line, '', current_time])  # Include the current time in the closing line

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

    return render_template('chat3.html', conversation=session['conversation'])

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    save_conversation_to_file()  # Save the current conversation
    session.clear() # clear the session

    # Create a response object from the rendered template
    response = make_response(render_template('bye.html', conversation=[]))

    # Set the session cookie to expire immediately
    response.set_cookie('session', '', expires=0)

    return response

def get_response(user_input):
    try:
        # Make the API call using the current conversation history
        response = client.chat.completions.create(
            # model="gpt-3.5-turbo",
            model="gpt-4-1106-preview",
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
