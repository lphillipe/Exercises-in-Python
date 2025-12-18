import requests
ACCESS_TOKEN = "BLABLA"


headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url, headers=headers)