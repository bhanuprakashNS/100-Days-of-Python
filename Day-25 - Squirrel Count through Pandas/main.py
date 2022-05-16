# .............................. Name Card ................................ #
# ............. Created and modified by N.S.Bhanuprakash on 01-04-2022 .....#

# with open("weather_data.csv") as weather_data:
#     weather_data = weather_data.readlines()
# print(weather_data)

# import csv
#
# with open("weather_data.csv") as data_csv:
#     data = csv.reader(data_csv)
#     # print(data)
#     temperatures = []
#     for row in data:
#         # print(row)
#         temp_in_row = row[1]
#         if temp_in_row != "temp":
#             temperatures.append(int(temp_in_row))
#     print(temperatures)

# Pandas examples .......................................
import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)

# data_dict = data.to_dict("list")
# temp_avg = data["temp"].mean()
# temp_max = data["temp"].max()
# print(temp_max)

# temp = data["temp"]
# # print(temp)
# # max_temp = data["temp"].max()
# max_temp_data = data[data["temp"] == 24]
# max_temp = int(max_temp_data.temp)
# max_temp_F = max_temp*9/5+32
# print(max_temp)
# print(max_temp_F)
#
# students = {"name": ["bhanu", "sukku", "pentamma"], "ranks": [2, 3, 1]}
# students_data = pandas.DataFrame(students)
# students_data.to_csv("students.csv")
# ...........................................................................

# Squirrel Data Analysis ....................................................

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_color = squirrel_data["Primary Fur Color"]
squirrel_color_list = squirrel_color.to_list()

# print(squirrel_data)
# print(squirrel_color)
# print(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"].count())

# print(squirrel_data["Primary Fur Color"].count())
# print(squirrel_color.count())
# print(squirrel_color_list.count("Gray"))

colors = ["Gray", "Cinnamon", "Black"]
squirrel_count = {"Fur Color": colors, "count": []}

for color in colors:
    squirrel_num = squirrel_color_list.count(f"{color}")
    squirrel_count["count"].append(squirrel_num)

print(squirrel_count)
squirrel_color_count_data = pandas.DataFrame(squirrel_count)
squirrel_color_count_data.to_csv("squirrel_color_data.csv")

# num_gray = 0
# num_cinnamon = 0
# num_black = 0
#
# for color in squirrel_color:
#     if color == "Gray":
#         num_gray += 1
#     elif color == "Cinnamon":
#         num_cinnamon += 1
#     elif color == "Black":
#         num_black += 1
# print(f"number of cinnamon squirrels are {num_cinnamon}, number of gray one are {num_gray}"
#       f" and the number of black squirrels are {num_black}")
