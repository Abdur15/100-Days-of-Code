from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 275)
        self.write(arg=f"Score = 0", font=("Arial", 15, "normal"), align="center")

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", font=("Arial", 15, "normal"), align="center")

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score = {self.score}", font=("Arial", 15, "normal"), align="center")
