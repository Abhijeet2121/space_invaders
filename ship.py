from turtle import Turtle

class Ship(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('turtle')
        self.color('light green')
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.penup()
        self.goto(position)
        self.speed(0)
        self.setheading(90)

    def go_right(self):
        x = self.xcor()
        if x < 250:
            x += 20
            self.setx(x)

    def go_left(self):
        x = self.xcor()
        if x > -250:
            x -= 20
            self.setx(x)
    
    def reset_position(self):
        self.goto(0,-230)
