from turtle import Screen, Turtle 
import random
import time
from ship import Ship

# Create screen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=500, height=500)
screen.title("Space Invadors")

# create ship
ship = Ship((0, -230))

# keyboard setting
screen.listen()
screen.onkey(ship.go_right, 'Right')
screen.onkey(ship.go_left, 'Left')
screen.exitonclick()