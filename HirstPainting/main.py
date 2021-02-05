# # colour extractor
# import colorgram
#
# colors = colorgram.extract('61RQCX9SJKL.jpg', 20)
#
# tot_colours = []
# for num in range(20):
#     colour = colors[num]
#     rgb = colour.rgb
#     red = rgb.r
#     green = rgb.g
#     blue = rgb.b
#     tot_colours.append(tuple([red, green, blue]))
#
# print(tot_colours)

# 10x10 rows of spots
# dot is 20 size
# spaced by 50 paces

import turtle as turtle_module
import random

turtle_module.colormode(255)
turt = turtle_module.Turtle()


colour_list = [(236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35), (6, 148, 93), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27)]

def random_colour():
    colour = random.choice(colour_list)
    return colour

turt.speed(10)
turt.setheading(225)
turt.penup()
turt.forward(250)
turt.setheading(0)
# print(type(turt.pos()))
position = turt.pos()

coord = 0
for num in range(1,11):
    turt.goto(position)
    turt.sety((turt.ycor() + coord))
    for dot in range(10):
        turt.dot(20, random_colour())
        turt.forward(50)
    coord = num * 50

turt.hideturtle()

screen = turtle_module.Screen()
screen.exitonclick()
