from turtle import Turtle

class Obstacle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.shape('square')
        self.color('light green')
        self.shapesize(0.1, 1)
        self.setheading(90)
        self.penup()
        self.goto(position)
        self.showturtle()

    