import time
from turtle import Screen, Turtle
from snake import Snake

screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("Snake game")

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

screen.exitonclick()