from turtle import Turtle, Screen

def create_custom_shape(image_path):
    screen = Screen()
    screen.register_shape(image_path)
    return image_path

class Bullet(Turtle):
    def __init__(self, position, ship, image_path):
        super().__init__()
        self.hideturtle()
        self.shape(create_custom_shape(image_path))
        self.color('white')
        self.shapesize(0.5,0.5)
        self.penup()
        self.goto(position)
        self.setheading(90)
        self.speed = 10
        self.ship = ship
        self.state = 'ready'

    def move(self):
        if self.state == 'fire':
            # y = self.ycor()
            # y += self.speed
            self.sety(self.ycor() + self.speed)

    def fire(self):
        if self.state == 'ready':
            self.state = "fire"
            self.goto(self.ship.position())
            self.showturtle()

    def is_collision(self, other):
        if self.distance(other) < 15:
            return True
        return False

    def reset_bullet(self):
        self.hideturtle()
        self.goto(self.ship.position())
        self.state = 'ready'



    # def move(self):
    #     if self.state == 'fire':
    #         y = self.ycor()
    #         y += self.speed()
    #         self.sety(y)

    # def fire_bullet(self):
    #     if self.state == 'ready':
    #         self.state = "fire"
    #         self.goto(self.ship.position())
    #         self.showturtle()

 


        