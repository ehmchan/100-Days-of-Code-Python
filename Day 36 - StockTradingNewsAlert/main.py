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

price_diff = abs(yes_close-before_yes_close)
five_perc = 0.05*yes_close

if price_diff >= five_perc:
    # print("Get News.")

    ## STEP 2: Use https://newsapi.org/docs/endpoints/everything
    # Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
    #HINT 1: Think about using the Python Slice Operator


    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()

    news_data = news_response.json()
    headlines = news_data["articles"][:3]
    print(headlines)


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # Send a separate message with each article's title and description to your phone number.
    #HINT 1: Consider using a List Comprehension.

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_=config.twilio_phone_num,
        to=config.my_phone_num
    )

    print((message.status))


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

