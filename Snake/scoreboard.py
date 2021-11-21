from turtle import Turtle

ALINGMENT = "center"
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.write_score()


    def write_score(self):
        self.write(arg=f"Score: {self.score}", move=False, align=ALINGMENT, font=FONT)

    def food_collision(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALINGMENT, font=FONT)



