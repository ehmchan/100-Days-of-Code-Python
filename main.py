import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()

screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.up, "Up")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    car_manager.create_car()
    car_manager.move_cars()

    #detect if turtle collides with car
    for car in car_manager.all_cars:
        if player.distance(car) < 30:
            game_is_on = False

    #detect when turtle hits top edge
    if player.ycor() > player.end_pos:
        player.reset_player()
        car_manager.increase_speed()



screen.exitonclick()
