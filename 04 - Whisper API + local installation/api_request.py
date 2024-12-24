import os
from openai import OpenAI
from dotenv import load_dotenv
from pydub import AudioSegment

# Ensure ffmpeg is installed and accessible
#audio = AudioSegment.from_mp3("./Meeting_Recording.mp3")

# PyDub handles time in milliseconds
#ten_minutes = 10 * 60 * 1000

#first_10_minutes = audio[:ten_minutes]

#first_10_minutes.export("./ai_10.mp3", format="mp3")

# Load environment variables from .env file
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"), 
)

audio_file = open("./ai_10.mp3", "rb")
transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
)

with open("README.md", "w", encoding="utf-8") as file:
    file.write(transcription.text)