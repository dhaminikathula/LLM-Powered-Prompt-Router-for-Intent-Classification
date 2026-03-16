import os
from dotenv import load_dotenv
from groq import Groq
from app.prompts import PROMPTS

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def route_and_respond(message, intent_data):

    intent = intent_data["intent"]

    # Manual override support
    if message.startswith("@code"):
        intent = "code"

    elif message.startswith("@data"):
        intent = "data"

    elif message.startswith("@writing"):
        intent = "writing"

    elif message.startswith("@career"):
        intent = "career"

    if intent == "unclear":

        return "I'm not sure what you need. Are you asking for help with coding, data analysis, writing, or career advice?"

    system_prompt = PROMPTS.get(intent)

    try:

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:

        print("ROUTER ERROR:", e)

        return "Sorry, an error occurred while generating the response."