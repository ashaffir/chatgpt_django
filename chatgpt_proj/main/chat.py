import openai

openai.api_key = "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"

def get_response(text):
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
