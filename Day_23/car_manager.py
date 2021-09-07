COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random
class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        create = random.randint(1, 6)
        if create == 1:
            car = Turtle()
            car.color(random.choice(COLORS))
            car.pu()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            y = random.randint(-250, 230)
            car.goto(300, y)
            self.cars.append(car)

    def car_move(self):
        for j in self.cars:
            j.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
























