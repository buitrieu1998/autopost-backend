from fastapi import APIRouter
from pydantic import BaseModel
import os
import requests

router = APIRouter(prefix="/post", tags=["post"])

class PostRequest(BaseModel):
    content: str
    platforms: list[str]

@router.post("")
def post_content(req: PostRequest) -> dict:
    results = {}
    for platform in req.platforms:
        name = platform.lower()
        if name == "facebook":
            results[name] = post_facebook(req.content)
        elif name == "twitter":
            results[name] = post_twitter(req.content)
        elif name == "tiktok":
            results[name] = post_tiktok(req.content)
        else:
            results[name] = {"error": "unsupported platform"}
    return results

def post_facebook(message: str) -> dict:
    token = os.getenv("FB_ACCESS_TOKEN")
    page_id = os.getenv("FB_PAGE_ID")
    if not token or not page_id:
        return {"error": "Facebook credentials missing"}
    resp = requests.post(
        f"https://graph.facebook.com/{page_id}/feed",
        params={"message": message, "access_token": token},
    )
    try:
        return resp.json()
    except Exception:
        return {"status": resp.status_code}

def post_twitter(message: str) -> dict:
    token = os.getenv("TWITTER_ACCESS_TOKEN")
    secret = os.getenv("TWITTER_ACCESS_SECRET")
    bearer = os.getenv("TW_BEARER_TOKEN")
    if not token or not secret or not bearer:
        return {"error": "Twitter credentials missing"}
    headers = {"Authorization": f"Bearer {bearer}"}
    data = {"text": message}
    resp = requests.post("https://api.twitter.com/2/tweets", json=data, headers=headers)
    try:
        return resp.json()
    except Exception:
        return {"status": resp.status_code}

def post_tiktok(message: str) -> dict:
    token = os.getenv("TIKTOK_ACCESS_TOKEN")
    if not token:
        return {"error": "TikTok token missing"}
    data = {"text": message, "access_token": token}
    resp = requests.post("https://open-api.tiktok.com/share/video", data=data)
    try:
        return resp.json()
    except Exception:
        return {"status": resp.status_code}
