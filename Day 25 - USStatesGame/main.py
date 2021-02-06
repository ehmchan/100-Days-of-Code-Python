import turtle
import pandas

data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_name = turtle.Turtle()
state_name.penup()
state_name.hideturtle()
state_name.speed("fastest")

# # get coordinates of states in image (ALREADY DONE, SAVED IN 50 STATES CSV)
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# use loop to allow user to keep guessing
game_is_playing = True
while game_is_playing:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

    # convert guess to title case
    guess = answer_state.title()

    # check if guess is among 50 states
    # write correct guesses onto map
    states = data["state"].to_list()
    if guess in states:
        state = data[data.state == guess]
        x_coord = int(state.x)
        y_coord = int(state.y)
        state_name.goto(x_coord, y_coord)
        state_name.write(guess, align="center", font=("Arial", 8, "normal"))


# record correct guesses in list

# keep track of score


screen.exitonclick()
