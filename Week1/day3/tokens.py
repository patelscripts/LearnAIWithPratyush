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
# 3 prompts
prompt1="Hii"
prompt2="Explain time travel in detail?"
prompt3="Write a 1000 words essay on the virat kohli?"
prompts=[prompt1, prompt2, prompt3]
for prompt in prompts:
    messages={
    "role" : role,
    "content": prompt
    }   
    messages = [messages]
    response = client.chat.completions.create(model=model, messages=messages, max_tokens=500)
    usage=response.usage
    print(f"Prompt : {prompt} --> Yours Token : {usage.prompt_tokens} --> completetion_token :{usage.completion_tokens} Finish Reason: {response.choices[0].finish_reason}")
#print(response.choices[0].message.content)