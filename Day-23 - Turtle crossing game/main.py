# ................... Turtle Crossing Game ................................ #
# ............. Created and modified by N.S.Bhanuprakash on 31-03-2022 .....#
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

car = CarManager()
player = Player()
screen.listen()
screen.onkey(player.up, "Up")
score = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.add_car()
    car.move()

    # Detection of Collision between player and the car
    for single_car in car.all_cars:
        if single_car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    # Has the player levelled up?
    if player.ycor() > (SCREEN_HEIGHT/2)-20:
        player.go_to_start()
        car.increase_speed()
        score.update_score()


screen.exitonclick()
