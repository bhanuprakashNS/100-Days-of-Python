# ....................... Snake Game ...................................... #
# ............. Created and modified by N.S.Bhanuprakash on 31-03-2022 .....#

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

my_screen = Screen()
screen_width = 600
screen_height = 600
my_screen.setup(width=screen_width, height=screen_height)
my_screen.bgcolor("black")
my_screen.tracer(0)

cookie = Snake()
food = Food()
score = Score()

my_screen.listen()
my_screen.onkey(cookie.up, "Up")
my_screen.onkey(cookie.down, "Down")
my_screen.onkey(cookie.right, "Right")
my_screen.onkey(cookie.left, "Left")

is_game_on = True
while is_game_on:
    my_screen.update()
    time.sleep(.2)
    cookie.move()

    # Detection with Food
    if cookie.head.distance(food) < 15:
        food.refresh()
        score.update_score()
        cookie.extend()

    # Detection with Wall
    if cookie.head.xcor() >= 290 or cookie.head.xcor() <= -290 or cookie.head.ycor() >= 290 or \
            cookie.head.ycor() <= -290:
        score.restart()
        cookie.restart()

    # Detection with Tail
    for segment in cookie.segments[1:]:
        if cookie.head.distance(segment) < 10:
            score.restart()
            cookie.restart()

my_screen.exitonclick()
