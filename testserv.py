import requests

print(
    requests.post(
        "https://research-assistant-vh2e.onrender.com",
        json={
            "query": "What is meta's new product Thread?"
        }
    ).json()
)