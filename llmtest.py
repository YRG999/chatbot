# llmtest.py
# Simple test of llm cli
# https://llm.datasette.io/en/stable/python-api.html

import llm
import os

model = llm.get_model("4t")
model.key = os.environ.get('OPENAI_API_KEY')
response = model.prompt("Why is the sky blue?")
print(response.text())