from turtle import Turtle
# Paddle inherits the Turtle class, to easily access and use all its methods and attributes

class Paddle(Turtle):
    # initializes the Paddle class => square shape, white color, size, and the position which differs for different sides
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    # moves the respective paddle up, on pressing the corresponding key => "Up" or "W"
    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    # moves the respective paddle down, on pressing the corresponding key => "Down" or "S"
    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
