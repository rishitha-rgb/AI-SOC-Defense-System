from fastapi import FastAPI
from firewall import firewall_check

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI SOC Defense System Running"}

@app.post("/analyze")
def analyze(request: str):

    if firewall_check(request):
        return {
            "status": "blocked",
            "reason": "Firewall detected attack pattern"
        }

    return {
        "status": "allowed",
        "message": "Request is safe"
    }
