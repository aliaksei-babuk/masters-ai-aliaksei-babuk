import os
from openai import OpenAI
from dotenv import load_dotenv

with open('transcript.txt', 'r') as file:
    content = file.read()

# Load environment variables from .env file
load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),  
)

response = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are a helpfull blockpost assistant, trained by OpenAI to help you write inspiring blogposts. You are usin BBC style."},
        {
            "role": "user",
            "content": "Write inspiring  blogpost about text below, focusing on the previous OpenAI news \n {content}",
        }

    ],
    model="gpt-4o-mini",
    temperature=0.7
)

with open('README.md', 'w') as file:
    print(response.choices[0].message.content, file=file)