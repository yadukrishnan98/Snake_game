from turtle import Turtle

class Snake:

    def __init__(self):
        self.segments = []
        self.step = 20
        self.create_snake()
        self.head = self.segments[0]
        

    def create_snake(self):
        x_pos = 0
        y_pos = 0

        for i in range(3):
            snake_block = Turtle(shape = 'square')
            snake_block.penup()
            snake_block.color('white')
            snake_block.goto(x=x_pos, y=y_pos)
            x_pos-=20
            self.segments.append(snake_block)

    def move(self):
            
        for i in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(self.step)


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
         

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
        

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
        
    
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    
    def add_new_block(self):
        new_block = Turtle(shape='square')
        new_block.penup()
        new_block.color('white')
        x_pos = self.segments[-1].xcor()
        y_pos = self.segments[-1].ycor()
        new_block.goto(x=x_pos, y=y_pos)
        self.segments.append(new_block)

    # Reset the snake
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        