import requests
import os
from dotenv import load_dotenv

load_dotenv()


class CallMeBot:


    def __init__(self):
        self.__base_url = 'https://api.callmebot.com/whatsapp.php'
        self.__api_key = os.getenv('API_KEY')
        self.__phone_number = os.getenv('TELL_KEY')

    def send_message(self, message):
        response = requests.get(
            url =f'{self.__base_url}?phone={self.__phone_number}&text={message}&apikey={self.__api_key}'
        )
        return response.json()