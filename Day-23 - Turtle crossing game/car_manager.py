from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
# INITIAL_CAR_SPEED = 0.1


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        # self.moving_speed = INITIAL_CAR_SPEED
        self.all_cars = []
        self.hideturtle()
        self.speed = STARTING_MOVE_DISTANCE

    def add_car(self):
        number = random.randint(1, 6)
        if number == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            y_cor = random.randrange(-260, 260, 20)
            new_car.goto((280, y_cor))
            # if len(self.all_cars) >= 2 and self.all_cars[-1].distance(self.all_cars[-2]) <= 40:
            #     # new_car.clear()
            #     print(self.all_cars[-1].position())
            #     # self.add_car()
            #     new_car.goto((280, y_cor + 20))
            #     print(.position())new_car
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def increase_speed(self):
        # self.moving_speed *= 0.9
        self.speed += MOVE_INCREMENT
        # STARTING_MOVE_DISTANCE += MOVE_INCREMENT
