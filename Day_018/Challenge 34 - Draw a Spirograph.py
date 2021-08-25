from turtle import Turtle,Screen
import random
screen = Screen()
screen.screensize(2000,1500)

my_turtle = Turtle()
my_turtle.shape("arrow")
my_turtle.speed("fastest")
my_turtle.hideturtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

for i in range(71):
    c = random.choice(colours)
    my_turtle.pencolor(c)
    my_turtle.circle(100)
    my_turtle.left(5)
    my_turtle.circle(100)




screen.exitonclick()
