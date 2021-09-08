from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.pu()
        self.color("white")
        self.setheading(90)
        self.setx(position)
        self.shapesize(1, 5)

    def up(self):
        self.setheading(90)
        self.forward(20)

    def down(self):
        self.setheading(270)
        self.forward(20)
