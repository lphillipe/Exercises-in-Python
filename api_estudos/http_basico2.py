import requests

url = "https://jsonplaceholder.typicode.com/posts"

url_tratada = requests.get(url)

dados = url_tratada.json()

print(type(dados))


#for dado in dados:
 #   print(dado)