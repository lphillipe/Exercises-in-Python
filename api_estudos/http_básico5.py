import requests

url = "https://jsonplaceholder.typicode.com/posts"

try:
    url_tratada = requests.get(url, timeout=)
except requests.exceptions.Timeout:5
    print("Erro: a requisição demorou muito (timeout)")

except requests.exceptions.RequestException:
    print("Erro: falha na requisição")