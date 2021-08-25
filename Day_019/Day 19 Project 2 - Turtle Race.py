from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)

tim = Turtle()
tim.hideturtle()
tim.penup()
tim.goto(x=195, y=-180)
tim.setheading(90)
tim.pendown()
tim.pensize(5)
tim.forward(360)
tim.penup()

start = False
color = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y_cor = [150, 100, 50, 0, -50, -100, -150]
turtles = []
for i in range(7):
    v = Turtle(shape="turtle")
    v.pu()
    v.goto(x=-230, y=y_cor[i])
    v.color(color[i])
    turtles.append(v)

usr = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter color:")
if usr:
    start = True
while start:
    for turtle in turtles:
        if turtle.xcor() > 200:
            start = False
            winner = turtle.pencolor()
            if winner == usr:
                print(f"You choose {usr} , You Won")
            else:
                print(f"The Winner is {winner}, You Lose")
            break
        s = random.randint(1, 10)
        turtle.forward(s)

screen.exitonclick()
