from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pw_box.delete(0, "end")
    pw_box.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_box.get()
    email = email_box.get()
    password = pw_box.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        # # day 29 old implementation
        # # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        # #
        # # if is_ok:
        #     # with open("data.txt", mode="a") as file:
        #     #     file.write(f"{website} | {email} | {password}\n")

        # no error handling
        # with open("data.json", "r") as file:
        #     # reading old data
        #     data = json.load(file)
        #     # updating old data with new data
        #     data.update(new_data)
        # with open("data.json", "w") as file:
        #     # saving updated data
        #     json.dump(data, file, indent=4)

        try:
            with open("data.json", "r") as file:
                # reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as file:
                # saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_box.delete(0, 'end')
            pw_box.delete(0, 'end')
            website_box.focus()

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_box.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            messagebox.showinfo(title=f"{website.title()}",
                                message=f"Email: {data[website]['email']} \nPassword: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exist.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=("Arial", 10, "normal"))
website_label.grid(column=0, row=1)

website_box = Entry(width=33)
website_box.grid(column=1, row=1)
website_box.focus()

email_label = Label(text="Email/Username:", font=("Arial", 10, "normal"))
email_label.grid(column=0, row=2)

email_box = Entry(width=51)
email_box.grid(column=1, row=2, columnspan=2)
email_box.insert(0, "eugenia@email.com")

pw_label = Label(text="Password:", font=("Arial", 10, "normal"))
pw_label.grid(column=0, row=3)

pw_box = Entry(width=33)
pw_box.grid(column=1, row=3)

generate_pw = Button(text="Generate Password", command=generate_password)
generate_pw.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
