from turtle import Turtle

class Bullet(Turtle):
    def __init__(self, position, ship):
        super().__init__()
        self.hideturtle()
        self.shape('circle')
        self.color('white')
        self.shapesize(0.5,0.5)
        self.penup()
        self.goto(position)
        self.setheading(90)
        self.state = 'ready'
        self.speed = 20
        self.ship = ship

    def move(self):
        if self.state == 'fire':
            y = self.ycor()
            y += self.speed
            self.sety(y)


    def fire(self):
        if self.state == 'ready':
            self.state = "fire"
            self.goto(self.ship.position())
            self.showturtle()

    def is_coliision(self, other):
        if self.distance(other) < 20:
            return True
        return False

    def reset_bullet(self):
        self.hideturtle()
        self.goto(self.ship.position())
        self.state = 'ready'
        self.direction = 'none'


        