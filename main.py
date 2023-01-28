from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # making it so we can use update()
screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()  # create a Snake object instance
food = Food()
scoreboard = Scoreboard()

screen.listen()  # want the screen to listen
screen.onkey(snake.up, "w")  # on keypres "w" call up function in snake class
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)

    snake.move() 
   
    # Detect Collision with foods

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    
    # Detect Colilision with Wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.display_game_over()
    
    # Detect Collision with Tail

    for segment in snake.seglist[1::]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.display_game_over()

screen.exitonclick()