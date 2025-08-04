from turtle import Turtle
from db import db_con

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0

        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()        

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.clear()
        self.score+=1
        self.update_score()

    
    def reset(self, user_name):
        if self.score > self.high_score:
            self.high_score = self.score
        db_con.insert_row(user_name, self.score, self.high_score)
        self.score = 0
        self.update_score()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER!", align="center", font=("Arial", 24, "normal"))
