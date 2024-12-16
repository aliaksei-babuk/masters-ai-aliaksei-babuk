import os
from openai import OpenAI
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"), 
)

response = client.images.generate(
        prompt="A vibrant and inspiring scene of a modern AI lab, showcasing advanced technology and AI models. The image includes a diverse team of AI researchers and developers collaborating on projects, with screens displaying complex algorithms, coding interfaces, and AI-generated images. The atmosphere is one of innovation and excitement. Hide a NINTENDO-style Easter egg",
        n=1,
        size="1024x1024",
        model="dall-e-3",
        quality="hd",
        style="natural"
)

image_url = response.data[0].url
print(image_url)

with open('README.md', 'w') as file:
    print(image_url, file=file)