#importing libraries
import smtplib
import pandas as pd
import datetime as dt
import random

#Set your email and password here. I removed mine for security reasons.
my_email = '<EMAIL>'
my_password = "<PASSWORD>"

#Sets today's date.
now= dt.datetime.today()
today = (now.month, now.day)

contact_list = pd.read_csv("birthdays.csv").to_dict(orient='records')

#Checks through the list to see if the month or day matches today, if it does, it creates a personalized letter and
#sends an email.
for contact in contact_list:
    if (contact['month'],contact['day']) == today:
        letter_number = random.randint(1,3)
        with open(f"letter_templates/letter_{letter_number}.txt","r") as f:
            letter= f.read()
            letter = letter.replace("[NAME]",contact['name'])
        with smtplib.SMTP('smtp.gmail.com',587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=my_password)
            connection.sendmail(from_addr=my_email,to_addrs=contact['email'],msg=f"Subject: Happy Birthday\n\n{letter}")