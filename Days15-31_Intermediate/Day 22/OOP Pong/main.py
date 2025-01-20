from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score

import time

#Sets up the screen and turns of auto animations.
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong in Python")
screen.bgcolor("black")
screen.tracer(0)

#Sets up the paddles and listens for key inputs to move them.
player_1 = Paddle(-350,0)
player_2 = Paddle(350,0)
screen.listen()
screen.onkey(player_1.p1up,"w")
screen.onkey(player_1.p1down,"s")
screen.onkey(player_2.p2up, key="Up")
screen.onkey(player_2.p2down,"Down")

#Sets up player 1 and 2 scores.
p1_score = Score(-150,250)
p2_score = Score(150,250)
ball = Ball()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.distance(player_2) < 60 and ball.xcor() > 320:
        ball.bounce_paddle()
    if ball.distance(player_1) < 60 and ball.xcor() < -320:
        ball.bounce_paddle()
    if ball.ycor() > 260:
        ball.bounce_wall()
    if ball.ycor() < -260:
        ball.bounce_wall()
    if ball.xcor() > 400:
        p1_score.point_scored()
        ball.reset_ball()
    if ball.xcor() < -400:
        p2_score.point_scored()
        ball.reset_ball()



screen.exitonclick()