from turtle import Screen, Turtle 
from ship import Ship
from enemy import Enemy
from bullet import Bullet
from enemy_fire import Enemy_fire
from level import Level
from scoreboard import Scoreboard
from lifes import Life
from obstacle import Obstacle
import random


# Images 
bg_pic = 'background.gif'
ship_img = 'ship.gif'
enemy_img = 'enemy.gif'
bullet_img = 'bullet.gif'
enemy_fire_img = 'enemy_fire.gif'
life_img = 'life.gif'

# Create screen
screen = Screen()
screen.bgcolor('black')
screen.bgpic(bg_pic)
screen.setup(width=750, height=750)
screen.title("Space Invadors")
screen.tracer(0)

#--------------------------------------------------------------------------#

# create ship
ship = Ship((0, -280), ship_img)

# create enemy 
enemies = []
enemy_rows = 3
enemy_columns = 8

def create_enemy():
    for row in range(enemy_rows):
        for column in range(enemy_columns):
            enemy_x = -200 + column * 50
            enemy_y = 250 - row * 50
            enemy_pos = (enemy_x, enemy_y)
            enemy = Enemy(enemy_pos, enemy_img)
            enemies.append(enemy)
create_enemy()

# create bullet
bullet = Bullet((0, -230), ship, bullet_img)

# initializing level
level = Level()

# score 
scoreboard = Scoreboard()

# # create lives
lives = 3
ship_lives = []
life_pos_x = -330
life_pos_y = 320

for l in range(lives):
    life = Life(life_pos_x, life_pos_y, life_img)
    ship_lives.append(life)
    life_pos_x += 20

# create enemy fire
enemy_fires = [Enemy_fire(enemy, ship, enemy_fire_img, bullet_speed=bullet.speed) for enemy in enemies]

# create obstacle
obstacles = []
obstacle_rows = 7
obstacle_columns = 30

def create_obstacle():
    for row in range(obstacle_rows):
        for column in range(obstacle_columns):
            obstacle_x = -200 + column * 15
            obstacle_y = 0 - row * 15
            obstacle_pos = (obstacle_x, obstacle_y)
            obstacle = Obstacle(obstacle_pos)
            # obstacle.create_pattern()
            obstacles.append(obstacle)
create_obstacle()

#--------------------------------------------------------------------------#

# keyboard setting
screen.listen()
screen.onkey(ship.go_right, 'Right')
screen.onkey(ship.go_left, 'Left')
screen.onkeypress(bullet.fire, 'space')

#---------------------------------------GAME LOGIC-------------------------#

game_is_on = True
while game_is_on:
    screen.update()

    # move the bullet
    bullet.move()

    # when bullet goes out of screen
    if bullet.ycor() > 350:
        bullet.reset_bullet()
    
    # move enemy 
    for enemy in enemies:
        enemy.move()

        # detect collision of enemy with wall
        if enemy.xcor() > 300 or enemy.xcor() < -300:
            for e in enemies:
                e.bounce_x()
            break

        # detect colission of enimies with each other 
        for other_enimies in enemies:
            if enemy != other_enimies and enemy.distance(other_enimies) < 20:
                enemy.bounce_x()
                other_enimies.bounce_x()

        # detect coliision between enemy and bullet
        if bullet.is_collision(enemy):
            enemy.goto(1000, 1000)
            enemies.remove(enemy)
            bullet.reset_bullet()
            scoreboard.increase_score()


    # Enemy fire bullets
    for enemy in enemies:
        if random.randint(0, 2000) == 1:
            enemy_fire = Enemy_fire(enemy, ship, enemy_fire_img, bullet_speed=bullet.speed)  # Create a new Enemy_fire object
            enemy_fire.fire()
            enemy_fires.append(enemy_fire)

    # Move enemy bullets
    for enemy_fire in enemy_fires:
        if enemy_fire.bullet.isvisible():
            enemy_fire.move_bullet()

        if enemy_fire.bullet.ycor() < -350:
            enemy_fire.reset_bullet()

        if enemy_fire.check_ship_collision():
            enemy_fire.reset_bullet()
            ship.reset_position()
            lives -= 1
            ship_lives[lives].hide()
            scoreboard.reset()


        # detect coliision between enemey bullet and ship bullet
        if bullet.state == "fire" and enemy_fire.bullet.isvisible():
            if enemy_fire.check_bullet_collision(bullet):
                bullet.reset_bullet()
                enemy_fire.reset_bullet()

        # increase the bullet speed with level increase and reset positions
        if len(enemies) == 0:
            level.increase_level()
            ship.reset_position()
            bullet.reset_bullet()
            bullet.speed += 1
            for enemy_fire in enemy_fires:
                enemy_fire.reset_bullet()
                
            
            create_enemy()
            create_obstacle()
            enemy_fires = [Enemy_fire(enemy, ship, enemy_fire_img, bullet_speed=bullet.speed) for enemy in enemies]


        # detect colision obstacles with bullet and enmy fire
        for obstacle in obstacles:
            if bullet.is_collision(obstacle):
                obstacles.remove(obstacle)
                obstacle.hideturtle()
                obstacle.goto(1000, 1000)
                bullet.reset_bullet()

            if enemy_fire.check_bullet_collision(obstacle):
                obstacles.remove(obstacle)
                obstacle.hideturtle()
                obstacle.goto(1000, 1000)
                enemy_fire.reset_bullet()

    if lives == 0:
        scoreboard.game_over()
        game_is_on = False
        break

        
screen.exitonclick()
