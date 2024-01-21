# llmtest2.py
# Simple test of llm cli with history
# https://llm.datasette.io/en/stable/python-api.html

import llm
import os

model = llm.get_model("4t")
model.key = os.environ.get('OPENAI_API_KEY')
conversation = model.conversation()
response = conversation.prompt("Five fun facts about pelicans")
print(response.text())

response2 = conversation.prompt("Now do skunks")
print(response2.text())