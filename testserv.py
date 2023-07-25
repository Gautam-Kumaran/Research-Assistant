import requests

print(" *********** going  got this ")

print(
    requests.get(        "http://127.0.0.1:8000"    ).content
)

print(" sfsdf  got this ")

print(
    requests.post(
        "http://127.0.0.1:8000",
        json={
            "query": "What is meta's new product Thread?"
        }
    ).json()
)