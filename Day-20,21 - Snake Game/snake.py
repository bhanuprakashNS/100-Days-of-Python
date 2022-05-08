from turtle import Turtle

SEGMENTS_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates a snake with 3 square segments"""
        for position in SEGMENTS_POSITION:  # Create a 3 dotted snake!
            self.add_segment(position)
        self.segments[0].shape("circle")
        self.segments[0].shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.segments[0].color("red")

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        # new_segment.speed("fast")
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Moves the snake by the amount of MOVING_DISTANCE"""
        for segment in range(len(self.segments) - 1, 0, -1):
            new_xcor = self.segments[segment - 1].xcor()
            new_ycor = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_xcor, new_ycor)
        self.head.forward(MOVING_DISTANCE)

    def restart(self):
        for seg in self.segments:
            seg.goto(-1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
