from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    # updates the scoreboard on the screen
    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # when game over = when snake collides with wall
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    # increases the score whenever the snake collides with food
    def increase_score(self):
        self.score += 1                 # first increase the score by 1
        self.clear()                    # clear the score screen, so they don't overlap
        self.update_score()             # now update the score screen
