from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=800)            # set up the screen's width and height
screen.title("Turtle Race")                     # sets the title of the screen

is_race_on = False
# receives the user's bet on which colored turtle will win in 'user_bet'
user_bet = screen.textinput("Make your bet", "Who will win the race? Choose a color ("
                                             "red/orange/green/purple/blue/grey):")
colors = ["red", "orange", "green", "purple", "blue", "grey"]
y_cord = [120, 80, 40, 0, -40, -80]
all_turtles = []

for x in range(6):
    new_turtle = Turtle(shape="turtle")         # create each obj of 'turtle' shape
    new_turtle.color(colors[x])                 # create each obj of a new color
    new_turtle.penup()                          # none of the turtles will have their pen down
    new_turtle.goto(x=-300, y=y_cord[x])        # all of them will be at the left edge, at different y coordinates
    all_turtles.append(new_turtle)              # appends each newly created turtle of the 'all_turtles' list

# after the user has placed his bet, the race is on
if user_bet:
    is_race_on = True

# until the race is on
while is_race_on:
    for turtle in all_turtles:
        # if the x coordinate of the turtle is 400, means it touched the right edge of the screen
        if turtle.xcor() == 300:
            is_race_on = False                          # since we have a winner, the race ends
            winning_color = turtle.pencolor()           # then retrieve the winning turtle's pencolor
            if winning_color == user_bet:
                print(f"Congrats! You won the bet! The {winning_color} turtle won.")
            else:
                print(f"Sorry.. You lost the bet! The {winning_color} turtle won.")

        rand_distance = random.randint(1, 10)      # every turtle will move a random dist. between 1 and 10
        turtle.forward(rand_distance)


screen.exitonclick()
