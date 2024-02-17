# anthropicbot

import os
import anthropic
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    # api_key="my_api_key",
    api_key=os.environ['ANTHROPIC_API_KEY']
)
message = client.messages.create(
    model="claude-2.1",
    max_tokens=1000,
    temperature=0,
    system="You are a helpful, cheerful assistant who always ends the conversation with a positive, uplifting word or phrase.",
    messages=[
        {"role": "user", "content": "Can you summarize PDFs?"}
    ]
)
print(message.content)

