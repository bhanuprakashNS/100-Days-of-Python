# ...................... Indian/US States Game/Quiz ................................ #
# ............. Created and modified by N.S.Bhanuprakash on 02-04-2022 ..............#
# This program displays an India or US states map and the student needs to write the state name correctly
# to score a point
from turtle import Turtle, Screen
import pandas
# .............Initialising turtle and the screen ..........#
my_screen = Screen()
cookie = Turtle()
state = Turtle()
image = "India_states_img.gif"
# "blank_states_img.gif"
states_data_file = "Indian_states_Coordinates.csv"
# "50_states.csv"
states_heading = "states"
# "state"
my_screen.addshape(name=image)
cookie.shape(name=image)
state.penup()
state.hideturtle()

# Reading the data(states and their coordinates) from the csv file created from "import_coordinates.py"
states_data = pandas.read_csv(states_data_file)
TOTAL_STATES = len(states_data)
# print(states_data)
score_count = 0
states_list = states_data[states_heading].tolist()
# print(states_list)


def ask_name(score):
    """a screen msg prompt asking the user to write the name of an Indian state"""
    if score == 0:
        title_name = "Guess the state"
    else:
        title_name = f"{score}/{TOTAL_STATES} states correct"
    name_prompt = my_screen.textinput(title=title_name, prompt="Guess a state name?").title()
    return name_prompt


def score_board(count=score_count):
    """Upgrading the score count if user(student or quiz participant) enters a correct Indian state name """
    count += 1
    return count


while score_count != TOTAL_STATES:
    state_name = ask_name(score_count)
    # print(state_name)
    for name in states_data[states_heading]:
        if state_name == name:
            # print("yes")
            score_count = score_board(score_count)
            x = float(states_data[states_data[states_heading] == state_name]['x'])
            y = float(states_data[states_data[states_heading] == state_name]['y'])
            position = (x, y)
            # print(position)
            state.goto(position)
            state.write(state_name)
            states_list.remove(state_name)

    if state_name == "Stop":
        break

# Writing the pending or left-over states to a csv file which needs to be learnt
states_left = pandas.DataFrame(states_list)
states_left.to_csv("states_to_learn.csv")
# exit()

my_screen.exitonclick()
