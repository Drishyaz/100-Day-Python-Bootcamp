from tkinter import *

window = Tk()                               # initialize the Tk() class
window.title("My First GUI Program")        # title() is used to set a custom title for the GUI window
window.minsize(width=500, height=300)       # minsize() sets a min height and width of the screen

# POSITIONING OF COMPONENTS AND WIDGETS
# pack()  -> positions the widget at the center; inflexible and unpredictable
# place() -> precise positioning; use x and y to set precise positions
# grid()  -> position with column and row; not as precise as place()
# DO NOT USE pack() and grid() in the same program

# PADDING AROUND COMPONENTS
# using config(padx=, pady=)
window.config(padx=20, pady=20)
# my_label.config(padx=20, pady=20)

# LABEL
my_label = Label(text="I am a Label", font=("Arial", 18, "italic"))
my_label.grid(column=0, row=0)
# my_label.pack()             # pack() automatically centers the component and places it on the screen

# user_input = input("What label do you want to show? ")
# # my_label["text"] = user_input
# my_label.config(text=user_input)


# BUTTON
def change_label(user_input):
    my_label["text"] = user_input


def input_detected():
    user_input = input.get()
    change_label(user_input)
    # print(user_input)


# Retrieve text input and change label every time the button is clicked
button = Button(text="Click", command=input_detected)
button.grid(column=1, row=1)
new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# ENTRY - Text Input Box
input = Entry()
# input.pack()
input.grid(column=3, row=2)

window.mainloop()           # mainloop() is the entry point of the GUI program that keeps its running

