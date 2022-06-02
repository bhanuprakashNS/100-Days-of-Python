# .................. Workout Tracker ................. #
# Created and modified by N.S.Bhanuprakash on 19-04-2022

import requests
from datetime import datetime
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME")
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutrition_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
exercise_input = input("Tell me what exercise you did?\n")
nutrition_parameters = {
    "query": exercise_input
}
response = requests.post(url=exercise_endpoint, json=nutrition_parameters, headers=nutrition_headers)
data = response.json()
print(data)

# Website(For Reference) - https://dashboard.sheety.co/projects/SHEETY_USERNAME/sheets/workouts
project_name = "workouts"  # name should be given in camelcase
sheet_name = "workouts"
sheety_endpoint = f"https://api.sheety.co/{SHEETY_USERNAME}/{project_name}/{sheet_name}"

sheety_header = {
    "Authorization": SHEETY_TOKEN
}

for num in range(len(data["exercises"])):
    # print(data["exercises"][num]["name"].title())
    now = datetime.now()
    # print(f"{now.date().strftime('%d/%m/%Y')}\n{now.time().strftime('%X')}")
    # print(data["exercises"][num]["duration_min"])
    # print(data["exercises"][num]["nf_calories"])
    sheety_parameters = {
        "workout": {
            "date": f"{now.date().strftime('%d/%m/%Y')}",  # Note that column headers like date, time - first letters
                                                           # are in small case
            "time": f"{now.time().strftime('%X')}",
            "exercise": f"{data['exercises'][num]['name'].title()}",
            "duration": f"{data['exercises'][num]['duration_min']}",
            "calories": f"{data['exercises'][num]['nf_calories']}",
        }
    }
    sheety_response = requests.post(url=sheety_endpoint, json=sheety_parameters, headers=sheety_header)
    # print(sheety_response.text)
    # print(sheety_response.url)
    print(sheety_response.raise_for_status())

