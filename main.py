from turtle import Screen, Turtle
from paddle import Paddle
import time

# create the screen
    # in main show
        # ping pong table

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

paddle = Paddle()
# create and move a paddle
    # separate class to create paddles
        # paddle 1
        # paddle 2

screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)



# create another paddle
# create the ball and make it move
    # separate class for ping pong
        # ping pong
# detect collision with wall and bounce
# detect collision with paddle
# detect when paddle misses
# keep score
    # separate class for scoreboard
        # scoreboard for each side



screen.exitonclick()

