from fastapi import FastAPI

from .routers import register as register_routers

app = FastAPI()

register_routers(app)


@app.get("/")
def root() -> dict:
    return {"message": "AutoPost Backend is running"}
