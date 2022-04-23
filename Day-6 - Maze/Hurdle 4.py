# .................. Reeborg's world Maze  .......................... #
# ...... Created and Modified by N.S.Bhanuprakash on 10-03-2022 ..... #

# https://reeborg.ca/reeborg.html?
# lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
def turnright():
    turn_left()
    turn_left()
    turn_left()
    # turn_left()


def jump():
    turn_left()
    while not right_is_clear():
        move()
    turnright()
    move()
    turnright()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()
