from turtle import Turtle
FONT = ("Arial", 16, "bold")
with open("high_score.txt", "r") as file:
    HIGH_SCORE = int(file.read())
#Creates a scoreboard to score our Snake game.
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.highscore = HIGH_SCORE
        self.score = 0
        self.goto(-50,270)
        self.color("White")
        self.write(f"Score: {self.score} High Score: {self.highscore}", font=FONT, align="center")

    #What happens if there is a game over.
    def reset(self):
        if self.score > int(self.highscore):
            self.highscore = str(self.score)
            with open("high_score.txt", "w") as file:
                file.write(self.highscore)
        self.score = 0
        self.update_scoreboard()

    #Increases the score each time we eat a food.
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=FONT)