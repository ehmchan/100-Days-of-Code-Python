from tkinter import *


def miles_to_km():
    km = round((float(input_miles.get()) * 1.609), 2)
    km_value_change.config(text=km)


window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=200, height=100)
window.config(padx=30, pady=30)

# label equal
equal_text = Label(text="is equal to", font=("Arial", 15, "normal"))
equal_text.grid(column=0, row=1)

# entry box for miles
input_miles = Entry(width=10)
input_miles.grid(column=1, row=0)

# label km value
km_value_change = Label(text="0", font=("Arial", 15, "normal"))
km_value_change.grid(column=1, row=1)

# calculate button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

# label miles unit
miles_text = Label(text="Miles", font=("Arial", 15, "normal"))
miles_text.grid(column=2, row=0)

# label km unit
km_text = Label(text="KM", font=("Arial", 15, "normal"))
km_text.grid(column=2, row=1)

window.mainloop()
