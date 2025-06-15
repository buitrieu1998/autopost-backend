import os
import openai
import requests


def generate_image(prompt: str, size: str = "1024x1024", filename: str = "generated.png") -> str:
    """Generate an image using OpenAI's API and save it locally."""
    openai.api_key = os.getenv("OPENAI_API_KEY")
    resp = openai.Image.create(prompt=prompt, n=1, size=size)
    url = resp["data"][0]["url"]
    r = requests.get(url)
    with open(filename, "wb") as f:
        f.write(r.content)
    return filename
