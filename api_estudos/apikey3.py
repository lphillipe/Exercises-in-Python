import requests
import os

token = os.environ.get("ACCESS_TOKEN")

headers = {
    "Authorization": f"Bearer {token}"
}

