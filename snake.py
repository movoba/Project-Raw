from turtle import Turtle


MOVE_SPEED = 20


class Snake:
    
    def __init__(self):
        self.snakes = []
        self.snake_start()
        self.head = self.snakes[0]
        

    def snake_start(self, x=0, y=0):
        for _ in range(3):
            snake = Turtle("square")
            snake.penup()
            snake.color("crimson")
            snake.goto(x , y)
            self.snakes.append(snake)
            x -= 20
            

    def move (self):
        for segnum in range(len(self.snakes) -1, 0, -1):
            neue_xcor = self.snakes[segnum - 1].xcor()
            neue_ycor = self.snakes[segnum - 1].ycor()
            self.snakes[segnum].goto(neue_xcor, neue_ycor)   
        self.head.forward(MOVE_SPEED)

    def add_segment(self):
        snake = Turtle("square")
        snake.penup()
        snake.color("crimson")
        snake.goto(self.snakes[-1].xcor(), self.snakes[-1].ycor())
        self.snakes.append(snake)
        
    
    def reset_all(self):
        snake = Turtle("square")
        snake.penup()
        snake.color("crimson")
        snake.goto(0,0)
        self.snakes.append(snake)
    
    def left(self):
        if self.head.heading() != 0:
            return self.head.seth(180)
            
    def up(self):
        if self.head.heading() != 270:
            return self.head.seth(90)
    
    def down(self):
        if self.head.heading() != 90:
            return self.head.seth(270)

    def right(self):
        if self.head.heading() != 180:
            return self.head.seth(0)
        