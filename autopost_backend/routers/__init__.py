from fastapi import FastAPI
from . import auth, content, posting


def register(app: FastAPI) -> None:
    app.include_router(auth.router)
    app.include_router(content.router)
    app.include_router(posting.router)
