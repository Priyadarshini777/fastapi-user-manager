# main.py
from fastapi import FastAPI

app = FastAPI(title="FastAPI User Manager - Demo")

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on GKE!"}

@app.get("/health")
def health():
    return {"status": "ok"}
