import turtle

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# # get coordinates of states in image (ALREADY DONE, SAVED IN 50 STATES CSV)
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
print(answer_state)

