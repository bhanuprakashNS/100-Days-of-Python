from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.write_score()

    def write_score(self):
        self.goto((-220, 250))
        self.write(arg=f"Level {self.score}", align="center", font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=("Arial", 40, "italic"))

