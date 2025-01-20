from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.body = []
        #Creates three square segments for the snake body.
        self.create_snake()
        #creates the head which is the first square segment.
        self.head = self.body[0]

    def create_snake(self):
        for i in range(3):
            new_square = Turtle("square")
            new_square.color("white")
            new_square.penup()
            new_square.setx(i * -20)
            self.body.append(new_square)
    def reset(self):
        for segment in self.body:
            segment.goto(1000, 1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]
    def extend(self):
        new_square = Turtle("square")
        new_square.speed("fastest")
        new_square.color("white")
        new_square.penup()
        new_square.setx(self.body[len(self.body) - 1].xcor())
        new_square.sety(self.body[len(self.body) - 1].ycor())
        self.body.append(new_square)

    def move(self):
        for numb_square in range(len(self.body) - 1, 0, -1):
            new_x = self.body[numb_square - 1].xcor()
            new_y = self.body[numb_square - 1].ycor()
            self.body[numb_square].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def down(self):
        if self.head.heading()!= UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)