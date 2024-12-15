from turtle import Turtle
FONT = ("Arial", 16, "bold")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.goto(-50,270)
        self.color("White")
        self.write(f"Score: {self.score}", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!!!", font=FONT, align="center")