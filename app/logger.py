import json
from datetime import datetime

LOG_FILE = "logs/route_log.jsonl"


def log_route(intent_data, message, response):

    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "intent": intent_data["intent"],
        "confidence": intent_data["confidence"],
        "user_message": message,
        "final_response": response
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")