from turtle import Turtle
class Snake:

    def __init__(self):
        self.turtles = []

    def create_snake(self):
        for i in range(3):
            tim = Turtle("square")
            tim.pu()
            tim.color('white')
            tim.setx(i * (-20))
            self.turtles.append(tim)

    def add_segment(self):
        tim = Turtle("square")
        tim.pu()
        tim.color('white')
        tim.setx(len(self.turtles) * (-20))
        self.turtles.append(tim)

    def move(self):
        for j in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[j - 1].xcor()
            new_y = self.turtles[j - 1].ycor()
            self.turtles[j].goto(new_x, new_y)
        self.turtles[0].forward(20)

    def reset(self):
        for i in self.turtles:
            i.goto(1000, 1000)
        self.turtles.clear()
        self.create_snake()

    def up(self):
        self.turtles[0].setheading(90)

    def down(self):
        self.turtles[0].setheading(270)

    def left(self):
        self.turtles[0].setheading(180)

    def right(self):
        self.turtles[0].setheading(0)
