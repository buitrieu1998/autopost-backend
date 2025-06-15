from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from . import ai, instagram, video

app = FastAPI()
templates = Jinja2Templates(directory="autopost_backend/templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/generate-image")
def generate_image(prompt: str = Form(...)):
    path = ai.generate_image(prompt)
    return {"image_path": path}


@app.post("/instagram/post")
def post_instagram(prompt: str = Form(...), caption: str = Form(...)):
    path = ai.generate_image(prompt)
    instagram.post_image_to_instagram(path, caption)
    return {"status": "posted"}


@app.post("/video/bulk-edit")
def bulk_edit_videos_endpoint(
    input_dir: str = Form(...), output_dir: str = Form(...), text: str = Form(...)
):
    video.bulk_edit_videos(input_dir, output_dir, text)
    return {"status": "processing"}
