from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(180)
        self.turtlesize(5)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(300,random.randint(-250,250))

    def move(self, level):
        self.forward(STARTING_MOVE_DISTANCE + (level * MOVE_INCREMENT) )