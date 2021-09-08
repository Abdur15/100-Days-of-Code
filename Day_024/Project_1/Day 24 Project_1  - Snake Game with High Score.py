from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
snake.create_snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.turtles[0].distance(food) < 15:
        food.refresh()
        snake.add_segment()
        score.score += 1
        score.update_score()
    if snake.turtles[0].xcor() > 270 or snake.turtles[0].xcor() < -270 or snake.turtles[0].ycor() > 270 \
            or snake.turtles[0].ycor() < -270:
        snake.reset()
        score.reset()
    for i in snake.turtles:
        if i == snake.turtles[0]:
            pass
        elif snake.turtles[0].distance(i) < 10:
            snake.reset()
            score.reset()
screen.exitonclick()
