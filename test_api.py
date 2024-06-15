import requests
import json


def main():
    url = "http://127.0.0.1:8000/items/"
    body = {
        "name": "Example Item",
        "description": "This is an example item.",
        "price": 29.99,
        "tax": 2.5,
    }
    res = requests.post(url,json.dumps(body))
    print(res.json())


if __name__ == "__main__":
    main()
