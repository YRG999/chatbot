# chat9.py updated with https://ollama.ai/blog/python-javascript-libraries

import ollama
response = ollama.chat(model='llama2', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
    # 'context': 'The time is midnight.'
  },
])
print(response['message']['content'])

# ollama.chat(model='llama2', messages=[{'role': 'user', 'content': 'Why is the sky blue?'}])

# import asyncio
# from ollama import AsyncClient

# async def chat():
#   message = {'role': 'user', 'content': 'Why is the sky blue?'}
#   async for part in await AsyncClient().chat(model='llama2', messages=[message], stream=True):
#     print(part['message']['content'], end='', flush=True)

# asyncio.run(chat())

# import ollama
# list = ollama.list()
# print(list)