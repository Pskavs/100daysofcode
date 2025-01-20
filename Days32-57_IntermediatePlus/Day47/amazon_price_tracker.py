#Importing packages needed.
import os
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
load_dotenv()
import smtplib

#Headers are used for the URL request so that the website doesn't automatically stop us from accessing data.
HEADERS = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "sec-ch-ua":'"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-platform': "Windows",
}
EMAIL = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

"""Accesses the data from the Amazon site, compares it to the price low point I've set, and then sends an email alert
with the price and the website."""
response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.text,'html.parser')
price = float(soup.find(class_="a-price-whole").text+ soup.find(class_='a-price-fraction').text)
print(price)
if price < 100:
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        message = f"""Subject: Price Drop Alert\n\n
        Price for your amazon item found at {URL} has dropped to ${price}."""
        connection.starttls()
        connection.login(EMAIL, EMAIL_PASSWORD)
        connection.sendmail(EMAIL, EMAIL, message)