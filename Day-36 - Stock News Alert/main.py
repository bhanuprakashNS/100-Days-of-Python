# ........................... Stock News Alert .......................................... #
# .............. Created and modified by NS Bhanuprakash on 15-04-2022 ............ #
# If the stock price variation > 5%, then a twilio sms alert is sent our mobile along with
# top 3 news headlines regd the company stock

import requests
from twilio.rest import Client
import html
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
alpha_endpoint = "https://www.alphavantage.co/query"
alpha_api_key = os.getenv("alpha_api_key")
alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alpha_api_key,
}
apinews_endpoint = "https://newsapi.org/v2/everything"
apinews_api_key = os.getenv("apinews_api_key")
apinews_parameters = {
    "q": COMPANY_NAME,
    "apiKey": apinews_api_key,
    "pageSize": 3
}
twilio_sid = os.getenv("sid")
twilio_auth_token = os.getenv("twilio_auth_token")
no_of_msgs = 3

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

data = requests.get(url=alpha_endpoint, params=alpha_parameters)
data.raise_for_status()
alpha_data = data.json()
yesterday = list(alpha_data["Time Series (Daily)"].keys())[0]
day_before_yesterday = list(alpha_data["Time Series (Daily)"].keys())[1]
stock_yesterday = float(alpha_data["Time Series (Daily)"][yesterday]["4. close"])
stock_day_before_yesterday = float(alpha_data["Time Series (Daily)"][day_before_yesterday]["4. close"])
percent_diff = round((stock_yesterday/stock_day_before_yesterday - 1)*100, 2)
abs_percent_diff = abs(percent_diff)
print(stock_yesterday, stock_day_before_yesterday, abs_percent_diff)

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

if abs_percent_diff > 5:
    print("get news!")
    data2 = requests.get(url=apinews_endpoint, params=apinews_parameters)
    data2.raise_for_status()
    # print(data2.url)
    news_data = data2.json()
    # print(news_data)
    for num in range(no_of_msgs):
        if percent_diff < 0:
            sign = "🔻"
        else:
            sign = "🔺"
        headline = html.unescape(f"Headline: {news_data['articles'][num]['title']}")
        brief = html.unescape(f"Brief: {news_data['articles'][num]['description']}")
        sms = f"{STOCK}: {sign}{abs_percent_diff}% \n{headline}\n{brief}"
        print(sms)
        
    # STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
        client = Client(twilio_sid, twilio_auth_token)
        message = client.messages \
            .create(
            body=sms,
            from_='+xxxxxxxxxxx',
            to='+91xxxxxxxxxx'
        )
        print(message.status)
