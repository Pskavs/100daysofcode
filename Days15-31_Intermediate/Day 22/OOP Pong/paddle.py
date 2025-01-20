import turtle
from turtle import Turtle

class Paddle(Turtle):
    paddles = []
    def __init__(self, start_x, start_y):
        super().__init__()
        #creates player 1 and 2 paddles and sets them to their side of the board.
        self.shape('square')
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(start_x, start_y)

    def p1up(self):
        self.goto(self.xcor(), self.ycor()+40)

    def p1down(self):
        self.goto(self.xcor(), self.ycor()-40)

    def p2up(self):
        self.goto(self.xcor(), self.ycor()+40)

    def p2down(self):
        self.goto(self.xcor(), self.ycor()-40)