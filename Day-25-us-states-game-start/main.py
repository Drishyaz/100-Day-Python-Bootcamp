# This is a game, where you can see a map of North America, and you have to guess its 50 states one by one
# India-state-game work is in progress. Soon that will be out too, so Indian locals can enjoy the state guessing too!
import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
# to add an image in your turtle screen
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
score = 0

while len(guessed_states) < 50:
    # Take the user's guess into ANSWER variable
    answer_state = screen.textinput(title=f"{score}/50 States correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:  # check if answer_state exists in data
        score += 1
        guessed_states.append(answer_state)
        t = turtle.Turtle()  # every time create a new turtle
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]  # get the row whose state == answer_state
        t.goto(int(state_data.x), int(state_data.y))  # get the x, y coordinates of that state
        t.write(arg=answer_state, font=("Arial", 12, "bold"))  # write the answer_state to that position

    # get the coordinates of all the states in the map
    # def get_mouse_click_coor(x, y):
    #     print(x, y)

    # from a mouse click, get the coordinates of that position
    # turtle.onscreenclick(get_mouse_click_coor)
    # the loop keeps running so the screen won't close
    # turtle.mainloop()

# states_to_learn.csv

