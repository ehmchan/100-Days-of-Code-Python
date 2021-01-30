from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

x=0
for num in range(3):
    new_segment = Turtle(shape="square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(x, 0)
    x-=20


screen.exitonclick()