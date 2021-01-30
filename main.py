from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)

# user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]

y = -100
for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colours[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y)
    y += 30
    turtle_index += 1




screen.exitonclick()