import requests
import datetime

TODAY = str(datetime.date.today()).replace('-','')
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = 'pskavs'
TOKEN = 'blah32forme'
GRAPH_ID = 'graph2025'
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# Created a username and password for this.
# response = requests.post(url=PIXELA_ENDPOINT, json=user_parameters)
graph_parameters = {
    "id": GRAPH_ID,
    'name': "Coding Tracker",
    'unit': 'hours',
    'type': 'float',
    'color': 'sora',
}
pixel_parameters = {
    'date':TODAY,
    'quantity':input("How many hours did you code today: "),
}
headers = {
    "X-USER-TOKEN": TOKEN,
}
update_parameters = {
    "quantity": "4",
}
# These two lines were used to create the graph
# graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)

# This is how you can add a point
graph_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
response = requests.post(url=graph_pixel_endpoint, json=pixel_parameters, headers=headers)
print(response.text)

# This is how you can update.
# update_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"
# response = requests.put(update_pixel_endpoint, headers=headers, json=update_parameters)
# print(response.text)

# Deletes a point.
# delete_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"
# response = requests.delete(delete_pixel_endpoint, headers=headers)
# print(response.text)