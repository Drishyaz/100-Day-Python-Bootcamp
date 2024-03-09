from turtle import Turtle, Screen

tim = Turtle()
tim.setheading(90)
tim.speed("fastest")
screen = Screen()
screen.listen()


def move_forward():
    tim.forward(20)


def move_backward():
    tim.backward(20)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def jump():
    tim.penup()
    tim.forward(50)
    tim.pendown()


def clear_screen():
    tim.clear()


screen.onkeypress(key="Up", fun=move_forward)
screen.onkeypress(key="Down", fun=move_backward)
screen.onkeypress(key="Left", fun=turn_left)
screen.onkeypress(key="Right", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
screen.onkey(key="space", fun=jump)

screen.exitonclick()
