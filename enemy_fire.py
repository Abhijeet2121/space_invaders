from turtle import Turtle, Screen

def create_custom_shape(image_path):
    screen = Screen()
    screen.register_shape(image_path)
    return image_path

class Enemy_fire:
    def __init__(self, enemy, ship, image_path, bullet_speed):
        self.enemy = enemy
        self.ship = ship
        self.bullet = Turtle()
        self.bullet.hideturtle()
        self.bullet.shape(create_custom_shape(image_path))
        self.bullet.color('yellow')
        self.bullet.shapesize(0.3, 0.6)
        self.bullet.setheading(270)
        self.bullet.penup()
        self.bullet.speed = bullet_speed
        # self.bullet.dy = 1 #set bullets on
        self.bullet.goto(self.enemy.position())

    def fire(self):
        self.bullet.showturtle()

    def move_bullet(self):
        self.bullet.forward(self.bullet.speed)

    def check_ship_collision(self):
        if self.bullet.distance(self.ship) < 15:
            self.ship.reset_position()
            return True
        return False

    def check_bullet_collision(self, other):
        if self.bullet.distance(other) < 15:
            self.reset_bullet()
            return True
        return False


    def reset_bullet(self):
        self.bullet.hideturtle()
        self.bullet.goto(self.enemy.position())
