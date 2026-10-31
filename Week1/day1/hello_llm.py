import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key is missing or not correct")

client = Groq(api_key=my_api_key)

model="openai/gpt-oss-120b"
role="user"
prompt="Do you know virat kohli?"
messages={
    "role" : role,
    "content": prompt
}
messages = [messages]
response = client.chat.completions.create(model=model, messages=messages)
print(response.choices[0].message.content)