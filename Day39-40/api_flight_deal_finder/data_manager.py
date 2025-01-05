import os
from dotenv import load_dotenv
import requests
from pprint import pprint
from requests.auth import HTTPBasicAuth

ENDPOINT = "https://api.sheety.co/37d17d22feeb25789fb1b204d09311be/flightDeals/prices/"
class DataManager:
    def __init__(self):
        load_dotenv()
        self._username = os.getenv("SHEETY_API_ID")
        self._password = os.getenv("SHEETY_API_KEY")


    def get_data(self):
        request = requests.get(ENDPOINT, auth=HTTPBasicAuth(self._username, self._password))
        request.raise_for_status()
        return request.json()

    def edit_data(self, flight):
        body = {
            "price": flight,
        }
        request = requests.put(url=f"{ENDPOINT}{flight['id']}", auth=HTTPBasicAuth(self._username, self._password), json=body)
        request.raise_for_status()
        return request.json()