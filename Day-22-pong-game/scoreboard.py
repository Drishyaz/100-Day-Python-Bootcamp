from turtle import Turtle, Screen
ALIGNMENT = "center"
FONT = ("Courier", 48, "normal")

# Scoreboard inherits the Turtle class, to easily access and use all its methods and attributes
class Scoreboard(Turtle):
    # initializes the scoreboard => white colored, penup, hidden turtle, etc
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    # updates the scoreboard as the points get updated
    def update_scoreboard(self):
        self.clear()
        self.goto(100, 200)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(-100, 200)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)

    # updates the left side's score, and calls the update method to update the scoreboard
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    # updates the right side's score, and calls the update method to update the scoreboard
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
