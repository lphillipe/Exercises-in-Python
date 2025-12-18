import requests
import os

token = os.environ.get("ACCESS_TOKEN")

headers = {
    "Authorization": f"Bearer {token}"
}

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url, headers=headers)
