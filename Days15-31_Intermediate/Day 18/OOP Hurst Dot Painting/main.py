import random
import colorgram
import turtle
from turtle import Screen


#This code was used to find the color of the image for our painting. It is no longer necessary.
# color_values =[]
# colors = colorgram.extract("image.jpg",15)
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     color_values.append((red, green, blue))
# print(color_values)

color_values = [(235, 38, 116), (215, 164, 59), (142, 27, 69), (237, 71, 36), (12, 142, 89), (179, 160, 47),
                (31, 123, 187), (176, 44, 99), (53, 189, 228), (243, 219, 53), (79, 21, 72)]

#Sets the turtle to the bottom left, and sets the color mode for rgb values.
turtle.hideturtle()
turtle.speed(0)
turtle.teleport(-200,-200)
turtle.colormode(255)
for row in range(1,11):
    for i in range(10):
        turtle.color(color_values[random.randint(0, len(color_values) - 1)])
        turtle.dot(20)
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
    turtle.teleport(-200,-200 + row*50)

screen = Screen()
screen.exitonclick()




#Challenge 1: turtle draws shapes increasing in size.
# sides = 8
# for i in range(3,sides+1):
#     tim.color(random.choice(turtle_colors))
#     turns = i
#     while turns != 0:
#         tim.right(360/i)
#         tim.forward(100)
#         turns -= 1

#Challenge 2: Random walk with Tim the Turtle
# tim.speed(15)
# tim.pensize(10)
# turtle.colormode(255)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b
#
# turn_direction = [0,90,180,270]
# while True:
#     tim.color(random_color())
#     travel = random.randint(0, 30)
#     tim.setheading(random.choice(turn_direction))
#     tim.forward(travel)
#

# Challenge 3 draws a spirograph in many different colors
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b
#
#
# for i in range(int(360/5 + 1)):
#     tim.color(random_color())
#     tim.circle(100)
#     tim.right(5)

