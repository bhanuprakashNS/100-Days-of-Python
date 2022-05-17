# .......... Indian/US States Game/Quiz - Creating coordinates for the Quiz ...................... #
# ............. Created and modified by N.S.Bhanuprakash on 02-04-2022 ............................#
# This program displays Indian states names in order and the teacher needs to click on that respective state location
# in order to record the coordinate for that state and save it for the Indian/US States Game/Quiz program
from turtle import Turtle, Screen
import pandas
import time
# .............Initialising turtle and the screen ........#
my_screen = Screen()
cookie = Turtle()
position_turtle = Turtle()
my_screen.addshape("India_states_img.gif")
cookie.shape("India_states_img.gif")
position_turtle.penup()
position_turtle.hideturtle()
position_turtle.goto(-280, 280)
# Creating states info dict and reading the data from the "Indian states names"
states_info = {"states": [], "x": [], "y": []}
states_data = pandas.read_csv("Indian states names.csv")
states_names = states_data["States"].tolist()
# print(len(states_names))

x_cor = []
y_cor = []
# print(states_info["x"])


def get_coordinates(x, y):
    """stores x and y coordinate values of mouse click on screen. This is for storing locations of states on map"""
    states_info["x"].append(x)
    states_info["y"].append(y)
    # x_cor.append(x)
    # y_cor.append(y)
    # print(x, y)
    # print(x_cor, y_cor)
    if x > 260:
        print("yes")
        my_screen.bye()


# Displaying all the state names one by one after a time delay of 5 sec.
# and allowing teacher(Quiz creator) to select those states locations on the screen in order to store it's x and y coors
num = 0
for state in states_names:
    position_turtle.clear()
    # if my_screen.onkey(fun=display, key="Right"):
    position_turtle.write(arg=state, align="center", font=("Arial", 16, "italic"))
    my_screen.onclick(get_coordinates)
    states_info["states"].append(state)
    time.sleep(5)
    print(num)
    # print(x_cor[num], y_cor[num])
    # states_info["X"].append(x_cor[num])
    # states_info["Y"].append(y_cor[num])
    num += 1
    my_screen.update()

states_info = pandas.DataFrame(states_info)
states_info.to_csv("Indian_states_Coordinates.csv")

my_screen.mainloop()

