import requests
import smtplib

#Global variables
NEWS_API_KEY = '<News API Key>'
STOCK_API_KEY = "<STOCK API>"
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"
GMAIL = "<EMAIL>"
GMAIL_PASSWORD = "<Password>"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters = {
    "apikey": STOCK_API_KEY,
    "symbol": STOCK_ENDPOINT,
    "function": "TIME_SERIES_DAILY",
}

news_parameters = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME,
    "pageSize": 10,
    "language": "en",
    "sortBy": "relevancy",

}

#I had to use the demo account to get around the free 25 a day limit for stocks. This creates a dictionary of stock close
# prices and then sees the percent change.
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'
request = requests.get(url)
request.raise_for_status()
stock_data = request.json()['Time Series (Daily)']
stock_dictionary = [value for (key, value) in stock_data.items()]
yesterday_close = stock_dictionary[0]['4. close']
day_before_close = stock_dictionary[1]['4. close']
percent = (float(yesterday_close) - float(day_before_close)) / float(yesterday_close)

# If the percent change is more than 5 percent, it sends an email with important news about the stock.
if abs(percent) > 0.05:
    request = requests.get(NEWS_ENDPOINT, params=news_parameters)
    request.raise_for_status()
    news_data = request.json()
    important_titles = []
    important_descriptions = []
    for news_item in news_data['articles']:
        if news_item['title'] == "[Removed]":
            del news_item
        else:
            important_titles.append(news_item['title'])
            important_descriptions.append(news_item['description'].encode('ascii', 'ignore').decode('ascii'))
    print(important_descriptions)
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=GMAIL, password=GMAIL_PASSWORD)
        connection.sendmail(
            from_addr=GMAIL,to_addrs=GMAIL,
            msg=f"Subject: Stock Daily Change \n\n {percent} change in {STOCK_NAME} \n\n Yesterday Close: {yesterday_close} "
                f"Today Close: {day_before_close} \n\n Important News:\n\n{important_titles[0]} : {important_descriptions[0]} "
                f"\n {important_titles[1]}: {important_descriptions[1]} \n "
                f"{important_titles[2]} : {important_descriptions[2]}"
        )
else:
    print("No major increases or decreases found.")