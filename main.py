from turtle import Screen, Turtle 
import random
import time
from ship import Ship
from bullet import Bullet
from enemy import Enemy

# Create screen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=500, height=500)
screen.title("Space Invadors")

# create ship
ship = Ship((0, -230))

# create enemy 
enemies = []
enemy_rows = 3
enemy_columns = 7

def create_enemy():
    for row in range(enemy_rows):
        for column in range(enemy_columns):
            enemy_x = -200 + column * 60
            enemy_y = 250 - row * 60
            enemy_pos = (enemy_x, enemy_y)
            enemy = Enemy(enemy_pos)
            enemies.append(enemy)

create_enemy()

# create bullet
bullet = Bullet((0, -230), ship)

# keyboard setting
screen.listen()
screen.onkey(ship.go_right, 'Right')
screen.onkey(ship.go_left, 'Left')
screen.onkeypress(bullet.fire, 'space')



###################################GAME LOGIC ##############################
game_is_on = True
while True:
    screen.update()

    # move the bullet
    bullet.move()

    # when bullet goes out of screen
    if bullet.ycor() > 260:
        bullet.reset_bullet()

    # move enemy 
    for enemy in enemies:
        enemy.move()

        # fire randomly
        if random.randint(1, 100) == 1:
            enemy.fire()

        # detect collision of enemy with wall
        if enemy.xcor() > 230 or enemy.xcor() < -230:
            for e in enemies:
                e.bounce_x()
            break

        # detect colission of enimies with each other 
        for other_enimies in enemies:
            if enemy != other_enimies and enemy.distance(other_enimies) < 20:
                enemy.bounce_x()
                other_enimies.bounce_x()

        # detect coliision between emeny and bullet
        if bullet.is_coliision(enemy):
            enemy.goto(1000, 1000)
            enemies.remove(enemy)
            bullet.reset_bullet()


screen.exitonclick()