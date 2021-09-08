from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle1 = Paddle(position=350)
paddle2 = Paddle(position=-350)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

game_is_on =True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    score.update()
    ball.refresh()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    if ball.distance(paddle1) < 50 and ball.xcor() < 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()
    if ball.xcor() > 350:
        ball.serve()
        score.l_point()

    if ball.xcor() < -350:
        ball.serve()
        score.r_point()

screen.exitonclick()