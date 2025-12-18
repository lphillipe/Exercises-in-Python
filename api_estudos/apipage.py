import requests

page = 1
limit = 5

params = {
    "_page": page,
    "_limit": limit
}

url ="https://jsonplaceholder.typicode.com/posts"

response = requests.get(url, params=params)

datas = response.json()

for data in datas:
    print(data["id"])
    print(data["title"])