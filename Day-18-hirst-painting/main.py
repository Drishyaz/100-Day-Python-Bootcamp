from turtle import Turtle, Screen
import random
import colorgram

# color extractor
colors = colorgram.extract('image.png', 30)
color_bank = []
# extracting the colors from the image and creating a tuple out of each of them
for color in colors:
    r = color.rgb.r     # color.rgb[0]
    g = color.rgb.g     # color.rgb[1]
    b = color.rgb.b     # color.rgb[2]
    color_tuple = (r, g, b)
    # color_string = tuple(color_string)
    color_bank.append(color_tuple)


# color_bank = [(104, 106, 125), (213, 152, 91), (140, 140, 150), (186, 62, 32), (225, 212, 109), (199, 147, 173),
# (237, 215, 225), (105, 112, 170), (177, 159, 47), (218, 224, 219), (186, 19, 9), (38, 40, 21), (27, 25, 63), (26,
# 42, 22), (223, 167, 194), (42, 44, 101), (205, 87, 58), (58, 68, 54), (132, 136, 132), (190, 187, 218), (230, 176,
# 172), (231, 65, 82)]
tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()


def center():
    # brings the turtle to the center of the screen
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)
    # 0 - East, 90 - North, 180 - West, 270 - South


def paint(num_of_dots):
    # paints a spot painting with the colors extracted
    for x in range(num_of_dots):
        for dot_count in range(num_of_dots):
            tim.dot(20, random.choice(color_bank))
            tim.forward(50)

        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        if num_of_dots % 10 == 0:
            tim.setheading(0)


center()
paint(10)

screen.exitonclick()
