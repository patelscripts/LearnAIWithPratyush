import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key is missing or not correct")

client = Groq(api_key=my_api_key)

model="openai/gpt-oss-120b"
role="user"

class Ticket(BaseModel):
    name:str
    email:str
    phone_Number:int
    address:str
schema=Ticket.model_json_schema()

response_format={
    "type":"json_object"
}
text="Hello my name is navneet patel. I have an PocoX7 phone . My address is lakhimpur kheri. My email is navneetpatel1234@gmail.com and my phone number is 8299560318"
prompt=f"""
This is a customer ticket. Please extract the personal information from this {text}
"""
system_prompt=f"""
Extract the personal information strictly based on this schema and give a json output {schema}
"""
message_system={
    "role" : "system",
    "content":system_prompt
}
messages={
    "role" : role,
    "content": prompt
}
messages = [message_system, messages]
response = client.chat.completions.create(model=model, messages=messages, temperature=1, response_format=response_format)
print(response.choices[0].message.content)