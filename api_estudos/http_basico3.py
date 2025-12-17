import requests

url = "https://jsonplaceholder.typicode.com/posts"

url_tratada = requests.get(url)

dados = url_tratada.json()

for dado in dados[:5]:
    print(dado["id"])
    print(dado["title"])