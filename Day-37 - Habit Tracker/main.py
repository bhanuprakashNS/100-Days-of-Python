# .......................... Habit Tracker ............................ #
# ........ Created and modified by N.S.Bhanuprakash on 16-04-2022 ..... #

import requests
import datetime
import pandas
import os

USER_NAME = "bhanuprakashns"
TOKEN = os.getenv("token")           # Api key
GRAPH_ID = "graph1"

# .................Creating an account using Post request ......#
pixela_endpoint = "https://pixe.la/v1/users"
pixela_parameters = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
response = requests.post(url=pixela_endpoint, json=pixela_parameters)
# print(response.json())
# print(response.text)

# ..................Creating the graph ...........#

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
graph_parameters = {
    "id": GRAPH_ID,
    "name": "Yoga",
    "unit": "min",
    "type": "int",
    "color": "shibafu"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# graph_response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(graph_response.url)
# print(graph_response.text)

# .................Today's date in required format .........#

today = datetime.datetime(year=2022, month=4, day=14)
date_modify = today.strftime("%Y%m%d")

# ................ Post(Create) Request ................#

get_graph_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
post_pixel_parameters = {
    "date": date_modify,
    "quantity": "45",
}
# pixel_post = requests.post(url=get_graph_endpoint, json=post_pixel_parameters, headers=headers)
# print(pixel_post.text)

# ........................ Put(Update) Request ...................#

graph_update_endpoint = f"{get_graph_endpoint}/{date_modify}"
graph_update_parameters = {
    "quantity": "45"
}
# pixel_update = requests.put(url=graph_update_endpoint, json=graph_update_parameters, headers=headers)
# print(pixel_update.text)

# ................ Delete Request .........................#

graph_delete_endpoint = f"{get_graph_endpoint}/{date_modify}"
# pixel_delete = requests.delete(url=graph_delete_endpoint, headers=headers)
# print(pixel_delete.text)

# .............Accessing my habit calendar and updating the pixels .....#

file = pandas.read_csv("Yoga_data.csv")
habit_record = file.to_dict("records")
print(file)
for record in range(len(file)):
    date = str(habit_record[record]["Date"])
    habit_quantity = str(habit_record[record]["Yoga(Min)"])

    graph_update_endpoint = f"{get_graph_endpoint}/{date}"
    graph_update_parameters = {
        "quantity": habit_quantity
    }
    pixel_update = requests.put(url=graph_update_endpoint, json=graph_update_parameters, headers=headers)
    # print(pixel_update.text)
