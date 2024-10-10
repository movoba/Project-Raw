from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.color("crimson")
        self.goto(-280,260)
        self.hideturtle()
        self.write(arg = f"Score: {self.score}" , move = False, align = "left", font = ("Arial", 20, "bold"))
        
        
    def punkte(self):
        self.score += 1
        self.write_neu()
        
    def write_neu(self):
        self.clear()
        self.write(arg = f"Score: {self.score}" , move = False, align = "left", font = ("Arial", 20, "bold"))
        
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(arg = f"GAME OVER \n Score: {self.score}", move = False, align = "center", font = ("Arial", 20, "bold"))
        