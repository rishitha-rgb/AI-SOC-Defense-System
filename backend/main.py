
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI SOC Defense System Running"}
