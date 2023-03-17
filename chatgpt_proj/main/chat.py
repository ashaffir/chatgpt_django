import openai
from django.conf import settings

openai.api_key = settings.OPENAI_KEY

def get_response(text):
    print(f"KY: {settings.OPENAI_KEY}")
    print(f"TEXT: {text}")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Dalai Lama."},
            {"role": "user", "content": f"{text}"},
            # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            # {"role": "user", "content": "Where was it played?"}
        ],
        temperature=0.15,
    )
    print(f"RES: {response}")
    return response
