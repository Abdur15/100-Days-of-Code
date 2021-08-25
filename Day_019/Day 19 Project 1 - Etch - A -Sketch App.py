from turtle import Turtle, Screen
screen = Screen()
screen.listen()
screen.screensize(2000, 1500)

my_turtle = Turtle()
my_turtle.shape("arrow")


def forward():
    my_turtle.forward(10)


def backward():
    my_turtle.backward(10)


def clockwise():
    my_turtle.right(10)


def counterclockwise():
    my_turtle.left(10)


def clr():
    my_turtle.pu()
    my_turtle.clear()
    my_turtle.home()
    my_turtle.pd()


screen.onkey(forward, "w")
screen.onkey(backward, "s")
screen.onkey(counterclockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clr, "c")


screen.exitonclick()
