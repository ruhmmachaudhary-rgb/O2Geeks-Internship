import requests

def generate(prompt):

    response = requests.post(
        "http://127.0.0.1:11434/api/generate",
        json={
            "model": "gemma3:1b",
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    if response.status_code == 200:
        return response.json()["response"]

    return "Error generating response."