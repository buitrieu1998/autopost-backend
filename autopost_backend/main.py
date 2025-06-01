from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "AutoPost Backend is running"}
