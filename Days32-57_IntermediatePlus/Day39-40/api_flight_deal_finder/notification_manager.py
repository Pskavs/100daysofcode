import os
import smtplib
from dotenv import load_dotenv

load_dotenv()
class NotificationManager:
# This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.email = os.environ.get('EMAIL')
        self.password = os.environ.get('EMAIL_PASSWORD')

    def send_email(self, price, to_flight, from_flight):
        """Takes the information from the flight, formats it into an email template, and then sends the information
        to the user's email address."""

        key_information = ['flight number', 'airport', 'time']
        to_information = [to_flight['number'],to_flight['departure']['iataCode'],to_flight['departure']['at']]
        from_information = [from_flight['number'],from_flight['departure']['iataCode'],from_flight['departure']['at']]

        #Creates two dictionaries in order to properly print the information.
        to_dictionary = dict(zip(key_information, to_information))
        from_dictionary = dict(zip(key_information, from_information))
        print(to_dictionary, from_dictionary)
        message = 'Departing Flight: \n'
        for key in to_dictionary:
            message+=f"{key}: {to_dictionary[key]}\n"

        message+='\nArriving Flight: \n'
        for key in from_dictionary:
            message+=f"{key}: {from_dictionary[key]}\n"

        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(self.email, self.password)
            message = f"Subject: Flight Deal Finder Notification\n\nPrice Drop: {price}\n{message}"
            connection.sendmail(
                from_addr=self.email,to_addrs=self.email,
                msg=message,

            )