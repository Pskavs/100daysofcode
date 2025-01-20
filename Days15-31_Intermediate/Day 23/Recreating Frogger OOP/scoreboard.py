from turtle import Turtle
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.teleport(-200,250)
        self.write(f"Level: {self.level}", align="center", font=FONT)
        self.hideturtle()

    def next_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over! Final Score: {self.level}", align="center", font=FONT)