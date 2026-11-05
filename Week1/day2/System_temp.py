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
prompt="suggest me a brand name for my E-commerce site "
message_system = {
    "role" : "system",
    "content":"you are a brand manager and you have a great knowledge about marketing. Give me only 5 names."
}
messages={
    "role" : role,
    "content": prompt
}
messages = [message_system, messages]
# temperature is by default is 0
response = client.chat.completions.create(model=model, messages=messages, temperature=0.2)
print(response.choices[0].message.content)