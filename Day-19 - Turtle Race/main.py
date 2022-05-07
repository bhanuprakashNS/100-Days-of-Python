# .................... Turtle Race and Etch a Sketch ................................ #
# .................. Created and modified by N.S.Bhanuprakash on 26-03-2022.......... #
from turtle import Turtle, Screen
import random

####################        Turtles Race            ##############################

is_race_on = False
screen = Screen()
width_screen = 600
height_screen = 400
screen.setup(width=width_screen, height=height_screen)
user_bet = screen.textinput(title="Make your bet", prompt="which color do you think will win?")

all_turtles = []
rainbow_colors = ["violet", "red", "blue", "green", 'yellow', "orange"]
turtle_y_pos = -(height_screen/2) + 50

for turtle_index in range(0, 6):                # Creating turtles of diff colors and giving their initial positions
    new_turtle = Turtle("turtle")
    new_turtle.color(rainbow_colors[turtle_index])
    new_turtle.penup()
    new_turtle.speed("fastest")
    turtle_y_pos += height_screen/len(rainbow_colors) - 20
    new_turtle.goto(x=-width_screen/2 + 20, y=turtle_y_pos)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:                           # Starting race and checking who wins!
    for racer in all_turtles:
        # racer.speed("fastest")
        if racer.xcor() >= width_screen/2 - 20:
            is_race_on = False
            racer_color = racer.pencolor()
            if racer_color == user_bet:
                print(f"You have won! The color of the winning turtle is {racer_color}")
            else:
                print(f"You have lost! The color of the winning turtle is {racer_color}")
        else:
            move_distance = random.randint(1, 10)
            racer.forward(move_distance)


screen.exitonclick()
########################################################################################################

########################     Etch_A_Sketch        ##################
# def forward():
#     tim.forward(50)
#
#
# def backward():
#     tim.back(50)
#
#
# def anti_clockwise():
#     tim.left(45)
#
#
# def clock_wise():
#     tim.right(45)
#
#
# def clear_screen():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# def move_forwards():
#     tim.forward(10)
#
#
# screen.listen()
# screen.onkey(key="space", fun=move_forwards)
# screen.onkey(key="w", fun=forward)
# screen.onkey(key="s", fun=backward)
# screen.onkey(key="a", fun=anti_clockwise)
# screen.onkey(key="d", fun=clock_wise)
# screen.onkey(key="c", fun=clear_screen)
# screen.exitonclick()
