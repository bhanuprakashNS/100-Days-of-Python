# ................... ISS Overhead ................................. #
# ..... Created and modified by N.S.Bhanuprakash on 12-04-2022 ..... #

import requests
from datetime import datetime
import smtplib
import time
import os

MY_LAT = 15.505723   # Your latitude 51.507351 15.505723
MY_LONG = 80.049919   # Your longitude 80.049919
from_email = "smtptrial22@gmail.com"
password = os.getenv("password")
smtp_server = "smtp.gmail.com"
guy_mail_id = "nsbprakash95@gmail.com"


def iss_nearby():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    near_latitude = False
    near_longitude = False
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
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

    time_now = datetime.now()
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True
    else:
        return False
# print(time_now, iss_longitude, iss_latitude, sunset)


while True:
    time.sleep(60)
    print("yes")
    if iss_nearby() is True and is_night() is True:
        # print("I am ISS and I am nearby and visible")
        letter_text = "I am ISS, I am nearby you and visible. Please go outside and look up"

        with smtplib.SMTP(smtp_server, 587) as connection:
            connection.starttls()
            connection.login(user=from_email, password=password)
            connection.sendmail(from_addr=from_email,
                                to_addrs=guy_mail_id,
                                msg=f"subject:ISS is nearby!\n\n"
                                    f"{letter_text}") 
