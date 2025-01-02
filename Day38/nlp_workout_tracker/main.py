#------------------------------Setting up Globals------------------------------------#
import datetime
import os
import pandas as pd
import requests

COMPANY_NAME = 'nutritionix'
HOST = 'https://trackapi.nutritionix.com'
ENDPOINT = '/v2/natural/exercise'

# Using pandas and a csv file to protect my information so people online can't see my API ID's and Keys.
data = pd.read_csv("C:/Users/pskav/OneDrive/Documents/API Keys/API's Free.txt").to_dict(orient='records')
api_info = []
for item in data:
    if item['company'].lower() == COMPANY_NAME.lower():
        api_info.append(item)

API_ID = os.environ.get('API_ID')
API_KEY = os.environ.get('API_KEY')

#------------------------------API Requests -------------------------------------------#

# Logs into nutritionix and asks the user what workouts they completed. It then uses NLP to determine the length of the
# workout and the calories burned.
nutritionix_headers = {
    'x-app-id': API_ID,
    'x-app-key': API_KEY,
}
nutritionix_body = {
    'query': input('What exercise did you complete?')
}
request = requests.post(url=HOST + ENDPOINT, headers=nutritionix_headers, json=nutritionix_body)
request.raise_for_status()

#Sets the information into variables to be added to a Google sheet.
exercise_data = request.json()['exercises']
exercise_name = exercise_data[0]['name']
exercise_duration = exercise_data[0]['duration_min']
exercise_calories = exercise_data[0]['nf_calories']

#Sets the time and date for today for tracking purposes.
import datetime
today = datetime.date.today().strftime('%d/%m/%Y')
time = datetime.datetime.now().strftime('%H:%M')
print(time,today)

# uses api to access the sheety website in order to overwrite my google sheets file.
sheety_url = 'https://api.sheety.co/37d17d22feeb25789fb1b204d09311be/myWorkouts2025/workouts'
sheety_header = {
    'Authorization': f'bearer {API_KEY}',
}
body = {
    "workout": {
        "date": str(today),
        "time": str(time),
        "exercise": exercise_name,
        "duration": float(exercise_duration),
        "calories": float(exercise_calories),
    }
}

response = requests.post(url=sheety_url, json=body,headers=sheety_header)

if response.status_code == 200:
    json_response = response.json()
    print(json_response.get("workout"))
else:
    print(f"Request failed with status code {response.status_code}: {response.text}")
