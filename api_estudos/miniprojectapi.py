import requests

url ="https://jsonplaceholder.typicode.com/posts"

page = 1
limit = 2
timeout = 5

params = {
    "_page": page,
    "_limit": limit
}

response = requests.get(url, params=params, timeout=timeout)