import requests

url = "https://jsonplaceholder.typicode.com/posts"

url_tratada = requests.get(url)

dados = url_tratada.json()

print(type(dados))

primeiro_item = dados[0]

print(primeiro_item["title"])
print(primeiro_item["body"])


#for dado in dados:
 #   print(dado)