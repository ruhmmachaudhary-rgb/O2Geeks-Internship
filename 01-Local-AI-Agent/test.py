import requests

response = requests.post(
    "http://127.0.0.1:11434/api/chat",
    json={
        "model": "gemma3:1b",
        "messages": [
            {
                "role": "user",
                "content": "What is AI?"
            }
        ],
        "stream": False
    },
    timeout=60
)

print(response.status_code)
print(response.json())