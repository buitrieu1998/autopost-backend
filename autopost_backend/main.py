from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root() -> dict:
    """Health check endpoint."""
    return {"message": "AutoPost Backend is running"}
