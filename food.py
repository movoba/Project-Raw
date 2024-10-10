import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self) ->None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("crimson")
        self.speed("fastest")
        x = random.randint(-280 , 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
        
    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)