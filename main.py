from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
viewport_w = screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("It's snaaaaaake")
screen.tracer(0)
screen.listen()
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
game_is_on = False

screen.onkey(fun = snake.left, key ="a")
screen.onkey(fun = snake.right, key = "d")
screen.onkey(fun = snake.down, key = "s")
screen.onkey(fun = snake.up, key = "w")

game_is_on = True
while game_is_on:
    
    if snake.head.distance(food) <= 15:
        food.refresh()
        scoreboard.punkte()
        snake.add_segment()
        scoreboard.save_highscore() 
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() >= 295 or snake.head.ycor() <= -295:
        game_is_on = False
        scoreboard.game_over()
        
        # lose = screen.textinput("You lost", "Nochmal Spielen?").lower()

        # if lose == "ja" or lose == "j" or lose == "yes" or lose =="y":
        #     scoreboard.write_neu()
        #     snake.head.goto(0,0)
        #     snake.head.seth(0)
        #     game_is_on = True
            
    for element in snake.snakes[1:]:
        if snake.head.distance(element) <= 15:
            game_is_on = False
            scoreboard.game_over()
            
            #lose
            # if lose == "ja" or lose == "j" or lose == "yes" or lose =="y":
            #     scoreboard.write_neu()
            #     snake.head.goto(0,0)
            #     snake.head.seth(0)
            #     game_is_on = True     scoreboard muss noch resettet werden und onkey nach gaame over geht noch nicht 
    screen.update()
    snake.move()
    time.sleep(0.1)
screen.exitonclick()