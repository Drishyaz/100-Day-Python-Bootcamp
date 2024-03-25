from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=100, pady=50)

# ENTRY(miles_input), LABEL("Miles"), LABEL("is equal to"), LABEL(converted_unit), LABEL("Km"), BUTTON("Calculate")

miles_input = Entry(width=20)
miles_input.grid(row=0, column=1)
miles_input.focus()

label_miles = Label(text="Miles")
label_miles.grid(row=0, column=2)


def convert():
    miles = float(miles_input.get())
    km_output = str(miles * 1.609)
    km_output_label.config(text=f"is equal to {km_output} Km")


km_output_label = Label(text=f"is equal to 0 Km", pady=10)
km_output_label.grid(row=1, column=1)

button = Button(text="Calculate", width=25, command=convert)
button.grid(row=2, column=1)

window.mainloop()
