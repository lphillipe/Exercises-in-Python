import requests

url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL"

get = requests.get(url)

print(get.status_code)


print("Hello World")
