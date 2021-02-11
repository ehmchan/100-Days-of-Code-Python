from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_box.get()
    email = email_box.get()
    password = pw_box.get()
    with open("data.txt", mode="a") as file:
        file.write(f"{website} | {email} | {password}\n")
        website_box.delete(0, 'end')
        pw_box.delete(0, 'end')
        website_box.focus()

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

website_box = Entry(width=51)
website_box.grid(column=1, row=1, columnspan=2)
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

generate_pw = Button(text="Generate Password")
generate_pw.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
