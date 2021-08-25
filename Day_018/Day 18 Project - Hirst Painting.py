import turtle
import colour_list
import random
from turtle import Turtle, Screen
screen = Screen()
screen.screensize(2000, 2000)
turtle.colormode(255)
colours = colour_list.rgb_colours

my_turtle = Turtle()
my_turtle.shape("arrow")
my_turtle.speed("fastest")
my_turtle.hideturtle()


def dotted():
    for i in range(10):
        my_turtle.dot(20, random.choice(colours))
        my_turtle.pu()
        my_turtle.forward(50)


for i in range(10):
    # print(my_turtle.pos())
    my_turtle.sety(50*i)
    my_turtle.setx(0)
    dotted()

screen.exitonclick()