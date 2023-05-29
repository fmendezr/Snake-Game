from scoreboard import Scoreboard
from snake import Snake
from food import Food
from turtle import Screen
import time

class SnakeGame():
    def __init__(self) -> None:

        # variable for controlling main loop
        self.game_ended = False

        # create and set up screen
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.tracer(0)

        # create scoreboard
        self.scoreboard = Scoreboard()

        # create snake
        self.snake = Snake()

        # create food
        self.food = Food()

        # add event listeners 
        self.screen.listen()
        self.screen.onkeypress(self.snake.turn_left, "Left")
        self.screen.onkeypress(self.snake.turn_right, "Right")

        #main loop
        self.main_looop()

        self.screen.exitonclick()
 
    # snake eats food 
    def detect_food(self):
        if self.snake.detect_collission_with_food(self.food):
            self.food.move_around()
            self.scoreboard.increment_score()

    # handle game over conditions
    def handle_game_over(self):
        if self.snake.detect_collission_with_self() or self.snake.detect_collission_with_wall():
            self.scoreboard.reset()
            self.snake.reset()
        
    # main game loop
    def main_looop(self):
        while not self.game_ended:
            self.screen.update()
            time.sleep(0.1)
            self.snake.move_forward()
            self.detect_food()
            self.handle_game_over()            
