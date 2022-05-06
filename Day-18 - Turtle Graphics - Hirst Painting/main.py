# ................. Turtle Graphics - Creating a Hirst painting ................................... #
# .................. Created and modified by N.S.Bhanuprakash on 26-03-2022 ....................... #


import random
import colorgram
from turtle import Turtle, Screen

my_screen = Screen()
my_screen.colormode(255)

cookie = Turtle()
cookie.shape("turtle")
# color = ["red", "orange", "blue", "green", "cyan", "dark green", "dark red"]
# cookie.color("Green")

rgb_colors = [(124, 101, 61), (166, 184, 196), (39, 27, 21), (167, 90, 220), (187, 155, 130), (20, 24, 30)]

# rgb_colors = []
# colors = colorgram.extract("Bhanu with Cock.jpg", 6)
# print(colors)
# # print(colors.rgb)
# for color in colors:                  # RGB color generator from a picture
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colour = (r, g, b)
#     rgb_colors.append(new_colour)
# print(rgb_colors)


# for _ in range(4):          # Draws a square
#     cookie.left(90)
#     cookie.forward(50)

# for _ in range(10):               # Creates a dashed line
#     cookie.forward(10)
#     cookie.penup()
#     cookie.forward(10)
#     cookie.pendown()


# def draw_polygon(no_sides):
#     """Takes the no.of sides as a parameter value and draws the polygon with respective no.of sides"""
#     turtle_angle = 360 / no_sides
#     side_length = 100
#     cookie.color(random.choice(color))
#     for _ in range(no_sides):
#         cookie.forward(side_length)
#         cookie.right(turtle_angle)
#
#
# for sides in range(3, 10):
#     draw_polygon(sides)


# def walk():
#     """ Generates a random walk in random direction """
#     angle = [0, 90, 180, 270]
#     cookie.setheading(random.choice(angle))
#     # cookie.color(random.choice(color))
#     side_length = 20
#     cookie.forward(side_length)
#
#
# turtle.colormode(255)
#
#
# def random_colour():
#     """Creates a tuple for colour randomly."""
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     colour = (r, g, b)
#     return colour


cookie.speed("fast")

# for _ in range(50):                                   # Creates a random walk with different colour and widths
#     cookie.color(random_colour())
#     cookie.width(random.randint(1, 10))
#     walk()

# tilt_angle = 45
# radius = 100
# for number in range(360//tilt_angle):                  # Creates a spirograph
#     cookie.color(random_colour())
#     current_angle = cookie.heading()
#     cookie.setheading(current_angle+tilt_angle)
#     cookie.circle(radius)


# cookie.circle(100)
# turtle.speed()
# turtle.penup()
# # turtle.home()
# turtle.goto(100,0)
# turtle.pendown()
# turtle.goto(-150,100)
# # turtle.reset()
# turtle.tilt(30)
# turtle.circle(50)

cookie.penup()                          # Creating a 10x10 dot paint
cookie.hideturtle()
x_cor = -300
y_cor = -200
cookie.setpos(x_cor, y_cor)

for _ in range(10):
    for _ in range(10):
        cookie.forward(50)
        cookie.dot(10, random.choice(rgb_colors))
        y_cor += 5
    cookie.setpos(x_cor, y_cor)

# print(my_screen.getshapes())
# print(my_screen.canvheight)
my_screen.exitonclick()
