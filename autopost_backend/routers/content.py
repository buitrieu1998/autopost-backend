from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import openai
import os

router = APIRouter(prefix="/content", tags=["content"])

class Prompt(BaseModel):
    prompt: str

@router.post("/generate")
def generate_content(data: Prompt) -> dict:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="OPENAI_API_KEY not configured")
    openai.api_key = api_key
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": data.prompt}]
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
    return {"content": resp.choices[0].message.content}
