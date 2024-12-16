import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#Creates scoreboard
scoreboard = Scoreboard()

#Sets up the screen, the player, and the cars
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()

#Creates a list to put the cars, and cycle. Every 6 cycles of the game, there will be another car generated.
cars = []
recycle_cars = []
cycle = 0

#This is how the player moves.
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")


game_is_on = True

#While the game is on it creates a new car every 0.6 seconds. If there are cars that have already made it to the
#end, they are recycled instead of the program creating more.
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if cycle == 6:
        cycle = 0
        #If there are any cars that can be recycled, they are used before creating more.
        if len(recycle_cars) > 0:
            recycle_cars[0].teleport(300,random.randint(-250,250))
            cars.append(recycle_cars[0])
            recycle_cars.remove(recycle_cars[0])
        else:
            new_car = CarManager()
            cars.append(new_car)
    cycle += 1
    for car in cars:
        car.move(scoreboard.level-1)
        #If the car hits the turtle, the game is ended and it prints the final score.
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
        if car.xcor() < -350:
            recycle_cars.append(car)
            cars.remove(car)
        if player.ycor() > 270:
            scoreboard.next_level()
            player.reset_player()
screen.exitonclick()