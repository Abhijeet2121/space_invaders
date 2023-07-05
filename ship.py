from turtle import Turtle, Screen

def create_custom_shape(image_path):
    screen = Screen()
    screen.register_shape(image_path)
    return image_path

class Ship(Turtle):
    def __init__(self, position, image_path):
        super().__init__()
        self.hideturtle()
        self.shape(create_custom_shape(image_path))
        self.color('light green')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(position)
        self.setheading(90)
        self.showturtle()

    def go_right(self):
        x = self.xcor()
        if x < 230:
            x += 20
            self.setx(x)

    def go_left(self):
        x = self.xcor()
        if x > -230:
            x -= 20
            self.setx(x)
    
    def reset_position(self):
        self.goto(0,-280)
