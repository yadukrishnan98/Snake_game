from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import Score
from db import db_con


'''Everything screen related is dealt with, in the main.py file'''

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Welcome to the snake game!")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()


user_name = screen.textinput(title='WELCOME TO THE SNAKE GAME', prompt='Enter your name')

# screen.listen()
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")


if user_name:
    is_game_on = True
else:
    is_game_on = False


def game_reset():
    global user_name
    score.reset(user_name)

    user_name = screen.textinput(title='WELCOME TO THE SNAKE GAME', prompt='Enter your name')

    if user_name:
        # score.reset(user_name)
        snake.reset()
        screen.listen()
        return True
    else:
        return False
    

def display_scores():
    
    high_scores = db_con.top_scores()

    if high_scores:
        print("\n" + "="*40)
        print("🏆 TOP 5 HIGH SCORES 🏆")
        print("="*40)
            
        for i, (name, high_score) in enumerate(high_scores, 1):
            print(f"{i}. {name:<15} - {high_score:>5} points")
            
        print("="*40)
    else:
        print("\nNo high scores recorded yet!")

    db_con.close()


while is_game_on:


    screen.update()
    time.sleep(0.1) #Screen updates every 0.1 second
    snake.move()

    
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    if snake.head.distance(food) < 15:
        food.gen_food()
        score.increase_score()
        snake.add_new_block()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # score.reset(user_name)
        # snake.reset()
        is_game_on = game_reset()

    for segment in snake.segments[1: len(snake.segments)]:
        if snake.head.distance(segment) < 10:
            # score.reset(user_name)
            # snake.reset()
            is_game_on = game_reset()


screen.exitonclick()

display_scores()