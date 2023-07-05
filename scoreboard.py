from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.highscore = int(data.read())
        self.color('white')
        self.penup()
        self.goto(-360, -320)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.highscore}", align='left', font=("courier", 16, 'normal'))

    def increase_score(self):
        self.score += 10
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt', mode='w') as data:
                data.write(f"{self.highscore}")
            self.score = 0
            self.update_scoreboard()
            
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align='center', font=('courier', 20, 'bold'))