from turtle import *
import random

screen = Screen()
screen.setup(width=500,height=400)

#Creates a dictionary of turtles with their colors and starting positions.
turtles = {
    "colors":["red", "blue", "green", "yellow", "purple"],
    "positions": [[-230,140],[-230,70],[-230,-0],[-230,-70],[-230,-140]]
}

#Makes sure the user bet is a color.
user_bet =''
while user_bet not in turtles['colors']:
    user_bet = screen.textinput(title="Make your bets:",prompt="Which turtle will win the race. Pick a color (red, blue, "
                                                   "green, yellow, or purple):")

#Creates a list of turtle objects of different colors and positions.
racing_turtles = []
def create_turtles():
    for i in range(0, 5):
        new_turtle = Turtle("turtle")
        new_turtle.color(turtles['colors'][i])
        new_turtle.penup()
        new_turtle.goto(turtles['positions'][i])
        racing_turtles.append(new_turtle)


#Starts the race. When a turtle reaches x coordinate 250, they are returned as the winner and it is compared to the bet.
def turtle_race():
    race_ongoing = True
    while race_ongoing:
        for racing_turtle in racing_turtles:
            racing_turtle.forward(random.randint(2,6))
            if racing_turtle.xcor() > 250:
                return racing_turtle.pencolor()

create_turtles()
winner = turtle_race()
if winner == user_bet.lower():
    print("You won! :)")
else:
    print("You lost! :(")
print(f"{winner} was the winner.")
screen.bye()
