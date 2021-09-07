from turtle import Turtle

class Road:
    def __init__(self):
        road_1 = Turtle()
        road_1.pu()
        road_1.goto(-300, -260)
        road_1.pd()
        road_1.pensize(7)
        road_1.forward(600)
        road_1.pu()
        road_1.goto(-300, 250)
        road_1.pd()
        road_1.pensize(7)
        road_1.forward(600)