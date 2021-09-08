from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', mode="r") as f:
            score = f.read()
            self.high_score = int(score)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 275)
        with open('data.txt', "r") as f:
            high_score = f.read()
        self.write(arg=f"Score = 0  High Score = {high_score}", font=("Arial", 15, "normal"), align="center")

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"GAME OVER", font=("Arial", 15, "normal"), align="center")

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', "w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score = {self.score} High Score = {self.high_score}", font=("Arial", 15, "normal"), align="center")
