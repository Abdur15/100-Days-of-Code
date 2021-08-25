from turtle import Turtle,Screen
screen = Screen()
screen.screensize(2000,1500)

my_turtle = Turtle()
my_turtle.shape("turtle")

def triangle():
    m = 0
    while m < 3:
        my_turtle.pencolor("red")
        my_turtle.forward(100)
        my_turtle.right(120)
        m+=1
def square():
    m = 0
    while m < 4:
        my_turtle.pencolor("blue")
        my_turtle.forward(100)
        my_turtle.right(90)
        m += 1
def pentagon():
    m = 0
    while m < 5:
        my_turtle.pencolor("yellow")
        my_turtle.forward(100)
        my_turtle.right(72)
        m += 1
def hexagon():
    m = 0
    while m < 6:
        my_turtle.pencolor("green")
        my_turtle.forward(100)
        my_turtle.right(60)
        m += 1
def heptagon():
    m = 0
    while m < 7:
        my_turtle.pencolor("violet")
        my_turtle.forward(100)
        my_turtle.right(51.42)
        m += 1
def octagon():
    m = 0
    while m < 8:
        my_turtle.pencolor("orange")
        my_turtle.forward(100)
        my_turtle.right(45)
        m += 1
def nanogon():
    m = 0
    while m < 9:
        my_turtle.pencolor("brown")
        my_turtle.forward(100)
        my_turtle.right(40)
        m += 1
def decagon():
    m = 0
    while m < 10:
        my_turtle.pencolor("pink")
        my_turtle.forward(100)
        my_turtle.right(36)
        m += 1

n=0
while n<1:
    triangle()
    square()
    pentagon()
    hexagon()
    heptagon()
    octagon()
    nanogon()
    decagon()
    n=+1

screen.exitonclick()
