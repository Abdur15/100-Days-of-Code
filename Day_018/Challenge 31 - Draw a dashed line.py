from turtle import Turtle,Screen

my_turtle = Turtle()
my_turtle.shape("turtle")


def dashed():
    my_turtle.forward(20)
    my_turtle.pu()
    my_turtle.forward(10)
    my_turtle.pd()
    my_turtle.forward(20)


n = 0
while n < 4:
    dashed()
    #my_turtle.right(90)
    n += 1


screen = Screen()
screen.exitonclick()