import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

# Get the api key from env
api_key = os.getenv("GEMINI_API_KEY")

# Configure gemini api
client = genai.Client(api_key=api_key)

print("Gemini configured.")

def generate_content(prompt: str):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception as error:
        raise RuntimeError(
            f"Failed to generate content: {error}"
        )
