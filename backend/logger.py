import json
from datetime import datetime

log_file = "../logs/logs.json"

def log_event(request,status):

    entry = {
        "time":str(datetime.now()),
        "request":request,
        "status":status
    }

    try:
        with open(log_file,"r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append(entry)

    with open(log_file,"w") as f:
        json.dump(logs,f,indent=4)
