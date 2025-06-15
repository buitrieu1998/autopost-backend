from fastapi import APIRouter, HTTPException
import os
import requests
from requests.auth import HTTPBasicAuth

router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/facebook")
def facebook_token() -> dict:
    app_id = os.getenv("FB_APP_ID")
    app_secret = os.getenv("FB_APP_SECRET")
    if not app_id or not app_secret:
        raise HTTPException(status_code=500, detail="Facebook credentials not configured")
    params = {
        "client_id": app_id,
        "client_secret": app_secret,
        "grant_type": "client_credentials",
    }
    resp = requests.get("https://graph.facebook.com/oauth/access_token", params=params)
    if resp.status_code != 200:
        raise HTTPException(status_code=resp.status_code, detail=resp.text)
    return resp.json()

@router.get("/twitter")
def twitter_token() -> dict:
    api_key = os.getenv("TW_API_KEY")
    api_secret = os.getenv("TW_API_SECRET")
    if not api_key or not api_secret:
        raise HTTPException(status_code=500, detail="Twitter credentials not configured")
    data = {"grant_type": "client_credentials"}
    auth = HTTPBasicAuth(api_key, api_secret)
    resp = requests.post("https://api.twitter.com/oauth2/token", data=data, auth=auth)
    if resp.status_code != 200:
        raise HTTPException(status_code=resp.status_code, detail=resp.text)
    return resp.json()

@router.get("/tiktok")
def tiktok_token() -> dict:
    client_key = os.getenv("TIKTOK_CLIENT_KEY")
    client_secret = os.getenv("TIKTOK_CLIENT_SECRET")
    if not client_key or not client_secret:
        raise HTTPException(status_code=500, detail="TikTok credentials not configured")
    data = {
        "client_key": client_key,
        "client_secret": client_secret,
        "grant_type": "client_credential"
    }
    resp = requests.post("https://open-api.tiktok.com/oauth/access_token", data=data)
    if resp.status_code != 200:
        raise HTTPException(status_code=resp.status_code, detail=resp.text)
    return resp.json()
