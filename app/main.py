from fastapi import FastAPI
from app.classifier import classify_intent
from app.router import route_and_respond
from app.logger import log_route

app = FastAPI()


@app.post("/chat")
def chat(message: str):

    intent = classify_intent(message)

    response = route_and_respond(message, intent)

    log_route(intent, message, response)

    return {
        "intent": intent,
        "response": response
    }