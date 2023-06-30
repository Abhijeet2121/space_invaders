from turtle import Turtle
from bullet import Bullet

class Enemy(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('turtle')
        self.color('blue')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(position)
        self.speed(0)
        self.setheading(270)
        self.x_move = 5
        self.y_move = 0

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def fire(self):
        bullet = Bullet((self.xcor(), self.ycor() - 20), 'yellow')
        bullet.move()

    def reset(self):
        self.hideturtle()
        self.goto((0, 230))
        self.showturtle()