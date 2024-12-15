import time
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("Snake in Python")
screen.setup(width=600, height=600)

# Turns off screen automatic update.
screen.tracer(0)

#Sets up the 3 squares.

snake = Snake()
screen.update()
snake_food = Food()

user_score = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Collision detection of snake with food.
    if snake.head.distance(snake_food) < 20:
        snake_food.move_food()
        snake.extend()
        user_score.increase_score()

    #Collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        user_score.game_over()

    #Collision with tail
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            user_score.game_over()
screen.exitonclick()