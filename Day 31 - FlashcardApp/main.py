from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("./data/french_words.csv")
words = data.to_dict(orient="records")

# create new flash cards
def create_cards():
    new_word = random.choice(words)
    canvas.itemconfig(language, text="French")
    canvas.itemconfig(word, text=new_word['French'])


# UI Setup
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=front_card)
language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_pic = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_pic, highlightthickness=0, command=create_cards)
wrong_button.grid(column=0, row=1)

right_pic = PhotoImage(file="./images/right.png")
right_button = Button(image=right_pic, highlightthickness=0, command=create_cards)
right_button.grid(column=1, row=1)

create_cards()

window.mainloop()
