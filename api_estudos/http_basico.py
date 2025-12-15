import requests

url = "https://jsonplaceholder.typicode.com/posts"

url_tratada = requests.get(url)

print(url_tratada.headers)

