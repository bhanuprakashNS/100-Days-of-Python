# ................... Pong-The-Arcade Game ............................. #
# ............. Created and modified by N.S.Bhanuprakash on 29-03-2022 .....#

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.title("Pong The Arcade")
my_screen.bgcolor("black")
my_screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()


my_screen.listen()
my_screen.onkey(fun=r_paddle.up, key="Up")
my_screen.onkey(fun=r_paddle.down, key="Down")
my_screen.onkey(fun=l_paddle.up, key="w")
my_screen.onkey(fun=l_paddle.down, key="s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    my_screen.update()
    ball.move()

    # Detection with top and bottom walls
    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce_y()

    # Detection with left and right paddles
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    # If ball misses the right paddle
    if ball.xcor() > 380:
        ball.reset()
        score.l_point()

    # If ball misses the left paddle
    if ball.xcor() < -380:
        ball.reset()
        score.r_point()

my_screen.exitonclick()
