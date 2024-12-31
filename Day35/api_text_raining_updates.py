import os
import requests
from twilio.rest import Client

#36,-115
#42, -94
api_key = os.environ.get("API_KEY")
weather_url = "http://api.openweathermap.org/data/2.5/forecast"
weather_params ={
    "lat": 42,
    "lon": -94,
    "appid": api_key,
    'cnt':4,
}

data = requests.get(weather_url, params=weather_params)
data.raise_for_status()

#Checks the next 4 forecasts (at 3 hour intervals) to see if there is any conditions for which we need an umbrella.
is_raining = False
for forecast in range(0,4):
    weather_data = data.json()['list'][forecast]['weather'][0]['id']
    if weather_data < 700:
        is_raining = True

if is_raining:
    print("Raining!")
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get("AUTH_TOKEN")

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+numberhere',
        body="It's going to rain today. Remember to bring an umbrella",
        to='whatsapp:+numberhere'
    )
    print(message.sid)
else:
    print("No Umbrella!!!")