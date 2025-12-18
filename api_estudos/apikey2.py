import requests
ACCESS_TOKEN = "BLABLA"


headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Sucessful Authorization")

elif response.status_code == in (401, 403):
    print("Wrong authorization")

else:
    print("Others errors")