FONT = ("Courier", 24, "normal")


from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.color("black")
        self.goto(-280, 265)
        self.level = 1
        self.update()

    def update(self):
        self.clear()
        self.write(arg= f"Level : {self.level}", font= FONT)
        self.level += 1
