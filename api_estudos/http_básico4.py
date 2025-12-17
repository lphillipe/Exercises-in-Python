import requests

url = "https://jsonplaceholder.typicode.com/posts"
url_fake = "https://jsonplaceholder.typicode.com/postsss"

url_tratada = requests.get(url_fake)

if url_tratada.status_code == 200:
    print("Sucesso")
else:
    print("Erro")