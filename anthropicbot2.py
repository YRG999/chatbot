# anthropicbot2
# from https://github.com/anthropics/anthropic-sdk-python?tab=readme-ov-file#usage

import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

client = Anthropic(
    # This is the default and can be omitted
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

message = client.messages.create(
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "How does a court case get to the supreme court?",
        }
    ],
    model="claude-2.1",
)
print(message.content)