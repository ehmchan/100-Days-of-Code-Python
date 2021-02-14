from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

words = {}
new_word = {}

# create new flash cards
def create_cards():
    global words, new_word, flip_timer

    try:
        data = pandas.read_csv("./data/words_to_learn.csv")
    except FileNotFoundError:
        data = pandas.read_csv("./data/french_words.csv")

    finally:
        words = data.to_dict(orient="records")
        window.after_cancel(flip_timer)
        new_word = random.choice(words)
        canvas.itemconfig(language, text="French", fill="black")
        canvas.itemconfig(word, text=new_word['French'], fill="black")
        canvas.itemconfig(canvas_image, image=front_card)
        flip_timer = window.after(3000, func=flip_card)

# flip cards
def flip_card():
    canvas.itemconfig(canvas_image, image=back_card)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=new_word['English'], fill="white")

# save progress
def know_words():
    words.remove(new_word)
    to_learn = words
    learn_data = pandas.DataFrame(to_learn)
    learn_data.to_csv("./data/words_to_learn.csv", index=False)
    create_cards()

# UI Setup
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_card)
language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(column=0, row=0, columnspan=2)

wrong_pic = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_pic, highlightthickness=0, command=create_cards)
wrong_button.grid(column=0, row=1)

right_pic = PhotoImage(file="./images/right.png")
right_button = Button(image=right_pic, highlightthickness=0, command=know_words)
right_button.grid(column=1, row=1)

create_cards()

window.mainloop()
