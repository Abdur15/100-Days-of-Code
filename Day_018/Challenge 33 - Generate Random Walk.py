from turtle import Turtle,Screen
import random
screen = Screen()
screen.screensize(2000,1500)

my_turtle = Turtle()
my_turtle.shape("arrow")
my_turtle.speed("fastest")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def right():
    my_turtle.right(90)
    k = random.randint(0,1)
    if k == 0:
        my_turtle.forward(20)
    else:
        my_turtle.backward(20)
def left():
    my_turtle.left(90)
    k = random.randint(0, 1)
    if k == 0:
        my_turtle.forward(20)
    else:
        my_turtle.backward(20)
n = 0
while n < 200:
        c = random.choice(colours)
        my_turtle.pensize(10)
        my_turtle.pencolor(c)
        m = random.randint(0,3)
        if m == 0:
            my_turtle.forward(20)
        elif m == 1:
            my_turtle.backward(20)
        elif m == 2:
            right()
        else:
            left()
        n += 1

screen.exitonclick()