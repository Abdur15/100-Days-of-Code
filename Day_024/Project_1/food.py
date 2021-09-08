from turtle import Turtle
import random

class Food (Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(0.5, 0.5)
        self.refresh()

    def refresh(self):
        rands = random.randint(-260, 260)
        randy = random.randint(-260, 260)
        self.goto(rands, randy)
