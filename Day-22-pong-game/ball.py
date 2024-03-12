from turtle import Turtle
# Ball inherits the Turtle class, to easily access and use all its methods and attributes

class Ball(Turtle):
    # initializes the Ball class => circle shape, white color, 20 pensize, etc
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pensize(20)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        # self.center_line()

    # moves the ball, changes its x_cor and y_cor by 10
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # reverses the direction of the ball everytime it hits the top or bottom edge
    def bounce_y(self):
        self.y_move *= -1           # reverses the direction

    # reverses the direction of the ball everytime it hits either of the paddles
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9      # everytime the ball hits the paddle, its speed increases

    # spawns the ball to center position, once a paddle misses to hit it
    def to_center(self):
        self.goto(0, 0)
        self.move_speed = 0.1       # when the paddle missed, the move_speed is reset
        self.bounce_x()

    # displays a center line in the screen
    def center_line(self):
        self.shape("square")
        self.shapesize(stretch_wid=50, stretch_len=0.3)
