# ..................... Birthday Wisher through email ....................... #
# .......... Created and modified by N.S.Bhanuprakash on 12-04-2022 ......... #

import pandas
import random
import smtplib
import datetime as dt
import os

from_email = "smtptrial22@gmail.com"
password = os.get_env("password")
smtp_server = "smtp.gmail.com"

# ToDo 1. Update the birthdays.csv and access the values

present_moment = dt.datetime.now()
present_day = present_moment.day
present_month = present_moment.month

birth_data = pandas.read_csv("birthdays.csv")

# ToDo 2. Check if today matches a birthday in the birthdays.csv

for index, row in birth_data.iterrows():
    if row["month"] == present_month and row["day"] == present_day:
        birthday_guy_name = row["name"]
        guy_mail_id = row["email"]

# ToDo 3. If step 2 is true, pick a random letter from letter templates

        choose_letter = random.randint(1, 3)
        with open(f"./letter_templates/letter_{choose_letter}.txt", "r") as new_file:
            lines = new_file.read()
            letter_text = lines.replace("[NAME]", birthday_guy_name)
            # letter_text = letter_text.replace("Happy birthday", "Belated Happy birthday")
# ToDo 4. Send the letter generated in step 3 to that person's email address.

        with smtplib.SMTP(smtp_server, 587) as connection:
            connection.starttls()
            connection.login(user=from_email, password=password)
            connection.sendmail(from_addr=from_email,
                                to_addrs=guy_mail_id,
                                msg=f"subject:Happy Birthday!\n\n"
                                    f"{letter_text}")
