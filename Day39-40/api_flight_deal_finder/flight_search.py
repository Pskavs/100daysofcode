import os
import requests
from dotenv import load_dotenv
import datetime

TOMORROW = str(datetime.date.today() + datetime.timedelta(days=1))
SIX_MONTHS = str(datetime.date.today() + datetime.timedelta(days=7))
LOCATION_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:
    def __init__(self):
        load_dotenv()
        self.iata_code = ""
        self.api_key = os.environ.get("AMADEUS_API_KEY")
        self.api_secret = os.environ.get("AMADEUS_API_SECRET")
        self.token = self.get_token()

    def get_token(self):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret,
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=headers, data=body)
        response.raise_for_status()
        data=response.json()["access_token"]
        return data


    def search_city(self,city):
        headers = {
            'Authorization': f"Bearer {self.token}",
        }

        body ={
            "keyword": city,
        }
        response = requests.get(url=LOCATION_ENDPOINT,headers=headers,params=body)
        response.raise_for_status()
        data = response.json()["data"][0]['iataCode']
        return data

    def find_flights(self,city):
        headers = {
            'Authorization': f"Bearer {self.token}",
        }

        body = {
            "currencyCode": "USD",
            "originLocationCode": "LAS",
            "destinationLocationCode": city,
            "departureDate": TOMORROW,
            'returnDate': SIX_MONTHS,
            'adults':1,
            'nonStop':"true",

        }
        response = requests.get(url=FLIGHT_ENDPOINT, headers=headers, params=body)
        response.raise_for_status()
        data=response.json()
        return data['data']