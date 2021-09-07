import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from road import Road

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.listen()
screen.tracer(0)

road = Road()
car = CarManager()
player = Player()
score = Scoreboard()
screen.onkey(player.turtle_move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.car_move()
    all_cars = car.cars

    if len(all_cars) > 0:
        for i in all_cars:
            if i.distance(player) < 30:
                game_is_on = False

    if player.ycor() > 260:
        score.update()
        player.player_refresh()
        car.level_up()





