import os
from pprint import pprint
from data_manager import *
from flight_search import *
from flight_data import*
import smtplib
import json
from notification_manager import*

notification_manager = NotificationManager()
get_flight = FlightSearch()

data_manager = DataManager()
sheet_data = data_manager.get_data()['prices']

for flight in sheet_data:
     if flight['iataCode'] == '':
         print(flight['id'])
         flight['iataCode'] = get_flight.search_city(flight['city'])
         data_manager.edit_data(flight)

for flight in sheet_data:
    flights = get_flight.find_flights(flight['iataCode'])
    if flights == []:
        print("No flight Found")
    else:
        flight_data = FlightData(flights)
        cheapest_flight = flight_data.find_cheapest_flight(flight)
        flight_price = cheapest_flight['price']['grandTotal']
        to_flight = cheapest_flight['itineraries'][0]['segments'][0]
        from_flight = cheapest_flight['itineraries'][1]['segments'][0]
        notification_manager.send_email(flight_price,to_flight,from_flight)

