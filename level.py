from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.color('white')
        self.goto(-360, -350)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align='left', font=('courier', 16, 'normal'))

    def increase_level(self):
        self.level += 1
        self.update_level()
