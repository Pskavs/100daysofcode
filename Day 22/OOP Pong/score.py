from turtle import Turtle

class Score(Turtle):
    def __init__(self, score_x, score_y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(score_x,score_y)
        self.write(f"{self.score}", align="center", font=("Arial", 24, "bold"))


    def point_scored(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", align="center", font=("Arial", 24, "bold"))
