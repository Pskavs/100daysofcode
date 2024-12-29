import pytz
import requests
from datetime import datetime
import smtplib
import time

#Latitude and Longitude of Las Vegas, Nevada
MY_LAT = 36.1716
MY_LONG = -115.1391

#Set your email and password here. I removed mine for security reasons.
my_email = '<EMAIL>'
my_password = "<PASSWORD>"

def check_iss():
    #Gets the latitude and longitude of the ISS
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Checks to see if Las Vegas' position is within +5 or -5 degrees of the ISS position.
    print(int(MY_LAT), int(MY_LONG), int(iss_latitude), int(iss_longitude))

    if MY_LAT - iss_latitude < 5 and MY_LONG - iss_longitude < 5:
        check_night()
    else:
        pass

def check_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    local_time = datetime.now()

    local_timezone = datetime.now().astimezone().tzinfo
    local_time = local_time.replace(tzinfo=local_timezone)

    utc_time = local_time.astimezone(pytz.utc)
    print(utc_time.hour,sunset, sunrise)
    if utc_time.hour >=sunset or utc_time.hour <= sunrise:
        print("it's night")
        #Emails user that they can see the space station if they look up.
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            connection.sendmail(
                from_addr=my_email,to_addrs=my_email,
                                msg="Subject:ISS!\n\n Look up! It's in the night sky"
            )
    else:
        #Too light to see the space station
        pass

while True:
    #Checks every 60 seconds while running.
    time.sleep(60)
    check_iss()