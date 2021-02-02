from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

# create the screen
    # in main

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

# create and move a paddle
    # separate class to create paddles
# create another paddle

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    # create the ball and make it move
    # separate class for ping pong
    ball.move()

    # detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


# detect when paddle misses
# keep score
    # separate class for scoreboard
        # scoreboard for each side



screen.exitonclick()

