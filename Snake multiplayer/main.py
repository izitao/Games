from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

#SNAKES STARTING POSITIONS CONFIGURATION
STARTING_POSITIONS_1 = [(80, 0), (60, 0), (40, 0)]
STARTING_POSITIONS_2 = [(-60, 0), (-80, 0), (-100, 0)]


#GAME OBJECTS
snake_1 = Snake("white", STARTING_POSITIONS_1)
snake_2 = Snake("red", STARTING_POSITIONS_2)
snakes = [snake_1, snake_2]

food_1 = Food()
food_2 = Food()
foods = [food_1, food_2]

#SCOREBOARD POSITIONS
SCORE_1_POSITION = (200, 280)
SCORE_2_POSITION = (-200, 280)

score_1 = Scoreboard("white", SCORE_1_POSITION)
score_2 = Scoreboard("red", SCORE_2_POSITION)
scores = {snake_1: score_1, snake_2: score_2}


#CONTROL CONFIGURATION
screen.listen()

screen.onkey(snake_1.up, "Up")
screen.onkey(snake_1.down, "Down")
screen.onkey(snake_1.left, "Left")
screen.onkey(snake_1.right, "Right")

screen.onkey(snake_2.up, "w")
screen.onkey(snake_2.down, "s")
screen.onkey(snake_2.left, "a")
screen.onkey(snake_2.right, "d")


#GAME LOOP
game_is_on = True
while game_is_on == True:
    screen.update()
    time.sleep(0.1)
    for snake in snakes:
        snake.move()

    #Detect collision with food
    for snake in snakes:
        for food in foods:
            if snake.head.distance(food) < 15:
                food.refresh()
                snake.extend()
                scores[snake].food_collision()


    #Detect collision with wall
    for snake in snakes:
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            score_1.game_over()

    #Detect collision with any part in the tail:
    for snake in snakes:
        for part in snake.snake_parts[1:]:
            if snake.head.distance(part) < 10:
                game_is_on = False
                score_1.game_over()

    #Detect snakes collision
    for part in snake_2.snake_parts[:]:
        if snake_1.head.distance(part) < 10:
            game_is_on = False
            score_1.game_over()

    for part in snake_1.snake_parts[:]:
        if snake_2.head.distance(part) < 10:
            game_is_on = False
            score_1.game_over()

screen.exitonclick()
