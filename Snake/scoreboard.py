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
        self.get_high_score()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALINGMENT, font=FONT)

    def food_collision(self):
        self.score += 1
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.write_score()
    
    def get_high_score(self):
        with open("data.txt", mode="r") as data:
            data = data.read()
            self.high_score = int(data)




