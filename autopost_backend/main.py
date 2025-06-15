from fastapi import FastAPI
from autopost_backend.routers import autopost_router

app = FastAPI()
app.include_router(autopost_router)

@app.get("/")
def root():
    return {"message": "AutoPost Backend is running"}
