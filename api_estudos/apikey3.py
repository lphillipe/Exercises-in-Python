import requests
import os

token = os.environ.get("ACCESS_TOKEN")

headers = {
    "Authorization": f"Bearer {token}"
}

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Successful Authorization")
elif response.status_code in (401, 403):
    print("Wrong Authorization")
else:
    print("Other errors")
