from fastapi import APIRouter
from pydantic import BaseModel
import os
import requests
from requests_oauthlib import OAuth1Session

router = APIRouter()

class PostRequest(BaseModel):
    message: str


def post_to_facebook(message: str) -> bool:
    page_id = os.getenv("FB_PAGE_ID")
    access_token = os.getenv("FB_ACCESS_TOKEN")
    if not page_id or not access_token:
        return False
    url = f"https://graph.facebook.com/v17.0/{page_id}/feed"
    data = {"message": message, "access_token": access_token}
    resp = requests.post(url, data=data)
    return resp.status_code == 200


def post_to_twitter(message: str) -> bool:
    api_key = os.getenv("TW_API_KEY")
    api_secret = os.getenv("TW_API_SECRET")
    access_token = os.getenv("TWITTER_ACCESS_TOKEN")
    access_secret = os.getenv("TWITTER_ACCESS_SECRET")
    if not all([api_key, api_secret, access_token, access_secret]):
        return False
    oauth = OAuth1Session(
        api_key,
        client_secret=api_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_secret,
    )
    url = "https://api.twitter.com/1.1/statuses/update.json"
    resp = oauth.post(url, params={"status": message})
    return resp.status_code == 200


@router.post("/post")
def create_post(req: PostRequest):
    fb = post_to_facebook(req.message)
    tw = post_to_twitter(req.message)
    return {"facebook": fb, "twitter": tw}

