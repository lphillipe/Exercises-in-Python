import requests

API_KEY = "My Key"

headers = {
    "Authorization": API_KEY
}

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Sucesso")
elif response.status_code == 401 or response.status_code == 403:
    print("Erro de Autenticação")
else:
    print("Outros erros")