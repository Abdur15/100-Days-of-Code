from turtle import Turtle,Screen

my_turtle = Turtle()
my_turtle.shape("turtle")

def square():
    n = 0
    while n < 4 :
        my_turtle.forward(100)
        my_turtle.right(90)
        n += 1

square()

# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

screen = Screen()
screen.exitonclick()