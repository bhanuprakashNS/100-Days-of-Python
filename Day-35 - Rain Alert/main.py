# ........................... Rain Alert .......................................... #
# .............. Created and modified by NS Bhanuprakash on 14-04-2022 ............ #
# Checks the weather data for the coming 12 hrs and alerts us through twilio sms if it's about to rain 

import requests
from twilio.rest import Client
import os

api_key = os.getenv("api_key")
MY_LAT = 25.2702
MY_LON = 91.7323
account_sid = os.getenv("sid")
auth_token = os.getenv("auth_token")
twilio_number = os.getenv("twilio_num")
parameters = {"lat": MY_LAT,
              "lon": MY_LON,
              "appid": api_key,
              "exclude": "current,minutely,daily"
}
api_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
one_call = requests.get(url=api_endpoint, params=parameters)
one_call.raise_for_status()
one_call_data = one_call.json()
total_hours = len(one_call_data["hourly"])
# hourly_weather_id = one_call_data["hourly"][hour]["weather"][0]["id"]
weather_id_data = [int(one_call_data["hourly"][hour]["weather"][0]["id"]) for hour in range(0, total_hours)]
weather_id_data = weather_id_data[:12]

check = all(x > 800 for x in weather_id_data)
if check is False:
    # print("Bring an umbrella!")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Don't forget to take your umbrella ☔",
        from_=twilio_number,
        to="+91-xxxxxxxxxx")
    print(message.status)
