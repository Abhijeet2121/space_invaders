from turtle import Turtle, Screen

def create_custom_shape(image_path):
    screen = Screen()
    screen.register_shape(image_path)
    return image_path

class Enemy(Turtle):
    def __init__(self, position, image_path):
        super().__init__()
        self.hideturtle()
        self.shape(create_custom_shape(image_path))
        self.color('blue')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.speed(0)
        self.goto(position)
        self.setheading(270)
        self.x_move = 1
        self.y_move = 0
        self.state = 'ready'
        self.showturtle()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def reset(self):
        self.hideturtle()
        self.goto((0, 230))
        self.showturtle()