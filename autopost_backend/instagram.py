import os
import requests

API_BASE = "https://graph.facebook.com/v19.0"


def post_image_to_instagram(image_path: str, caption: str):
    """Post an image to Instagram using the Graph API."""
    access_token = os.getenv("IG_ACCESS_TOKEN")
    account_id = os.getenv("IG_ACCOUNT_ID")
    if not access_token or not account_id:
        raise ValueError("Instagram credentials not configured")

    # This implementation assumes the account is connected to Facebook page
    upload_url = f"{API_BASE}/{account_id}/media"
    with open(image_path, "rb") as f:
        files = {"image_file": f}
        data = {"caption": caption, "access_token": access_token}
        res = requests.post(upload_url, files=files, data=data)
    res.raise_for_status()
    creation_id = res.json().get("id")

    publish_url = f"{API_BASE}/{account_id}/media_publish"
    publish_res = requests.post(publish_url, data={"creation_id": creation_id, "access_token": access_token})
    publish_res.raise_for_status()
    return publish_res.json()
