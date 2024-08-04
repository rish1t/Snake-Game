import time
from turtle import Turtle, Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
x = 0
y = 0

positions = []
segments = []

snaku = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkeypress(snaku.up, "Up")
screen.onkeypress(snaku.down, "Down")
screen.onkeypress(snaku.left, "Left")
screen.onkeypress(snaku.right, "Right")

screen.update()
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    snaku.move()

    if snaku.segments[0].distance(food) < 15:
        food.refresh()
        snaku.extend()
        score.increase_score()

    if snaku.segments[0].xcor() > 280 or snaku.segments[0].xcor() < -280 or snaku.segments[0].ycor() > 280 or snaku.segments[0].ycor() < -280:
        game_on = False
        score.game_over()

    for segment in snaku.segments:
        if segment == snaku.segments[0]:
            pass
        elif snaku.segments[0].distance(segment) < 10 :
            game_on: False
            score.game_over()
screen.exitonclick()