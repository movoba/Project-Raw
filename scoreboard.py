from turtle import Turtle
PATH ="Lv 20 Snake Game/Project Raw/data.txt"

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self. highscore = 0
        with open("data.txt") as file:
            inhalt = file.read()
            if inhalt:
                self.highscore = int(inhalt)
        self.penup()
        self.color("crimson")
        self.goto(-280,260)
        self.hideturtle()
        self.write(arg = f"Score: {self.score} Highscore: {self.highscore}" , move = False, align = "left", font = ("Arial", 20, "bold"))
        
    def punkte(self):
        self.score += 1
        self.write_neu()
        
    def write_neu(self):
        self.clear()
        self.write(arg = f"Score: {self.score} Highscore: {self.highscore}" , move = False, align = "left", font = ("Arial", 20, "bold"))
        
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(arg = f"GAME OVER \n Your Score: {self.score} \n Highscore Score: {self.highscore}", move = False, align = "center", font = ("Arial", 20, "bold"))
        
    def save_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
        with open("data.txt", mode="w") as file:
            file.write(f"{self.highscore}")