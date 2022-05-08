from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 30, "italic")


class Score(Turtle):
    """Initialises scoreboard, updates it and prompts when Game is over!"""

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/NSBP/Python for Everybody/100 Days of Code/high_score_value.txt") as high_score:
            high_score_value = high_score.read()
        self.high_score = int(high_score_value)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.score_board()

    def score_board(self):
        self.write(f"score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.score_board()

    def restart(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
        with open("/NSBP/Python for Everybody/100 Days of Code/high_score_value.txt", "w") as high_score:
            high_score.write(str(self.high_score))

        self.score = 0
        self.score_board()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
