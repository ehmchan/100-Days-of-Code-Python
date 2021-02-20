import requests
from datetime import datetime, timedelta
from twilio.rest import Client
import config

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_api = config.stock_api
news_api = config.news_api
account_sid = config.twilio_account_sid
auth_token = config.twilio_auth_token

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api,
}

news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": news_api
}

yesterday = datetime.date(datetime.now()) - timedelta(1)
before_yes = datetime.date(datetime.now()) - timedelta(2)

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()

stock_data = stock_response.json()
yes_close = float(stock_data["Time Series (Daily)"][str(yesterday)]["4. close"])
before_yes_close = float(stock_data["Time Series (Daily)"][str(before_yes)]["4. close"])

price_diff = yes_close-before_yes_close
perc_diff = round((abs(price_diff)/yes_close)*100)
if price_diff < 0:
    delta = "🔻"
elif price_diff > 0:
    delta = "🔺"

if perc_diff >= 5:
    # print("Get News.")

    ## STEP 2: Use https://newsapi.org/docs/endpoints/everything
    # Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
    #HINT 1: Think about using the Python Slice Operator
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()

    news_data = news_response.json()
    headlines = news_data["articles"][:3]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # Send a separate message with each article's title and description to your phone number.
    #HINT 1: Consider using a List Comprehension.
    for headline in headlines:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"""
                {STOCK}: {delta}{perc_diff}%
                Headline: {headline["title"]}
                Brief: {headline["description"]}
                """,
            from_=config.twilio_phone_num,
            to=config.my_phone_num
        )

        print((message.status))
