from turtle import Turtle, Screen

def create_custom_shape(image_path):
    screen = Screen()
    screen.register_shape(image_path)
    return image_path

class Life(Turtle):
    def __init__(self, x , y, image_path):
        super().__init__()
        self.shape(create_custom_shape(image_path))
        self.penup()
        self.color('red')
        self.setheading(90)
        self.shapesize(0.4, 0.6)
        self.goto(x , y)
        self.showturtle()

    def hide(self):
        self.hideturtle()