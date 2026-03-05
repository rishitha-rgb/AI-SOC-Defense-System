from fastapi import FastAPI
from firewall import firewall_check
from detector import predict_attack
from logger import log_event

app = FastAPI()

@app.get("/")
def home():
    return {"message":"AI SOC Defense Platform"}

@app.post("/analyze")
def analyze(request:str):

    if firewall_check(request):
        status = "blocked by firewall"
        log_event(request,status)
        return {"result":status}

    prediction = predict_attack(request)

    if prediction == "attack":
        status = "blocked by AI"
    else:
        status = "allowed"

    log_event(request,status)

    return {"result":status}
