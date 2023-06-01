from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.high_score = self.get_high_score()
        self.color("white") 
        self.penup()
        self.hideturtle()
        self.goto(0, 265)
        self.write_score()
        self.get_high_score()
    
    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Verdana", 25, "normal"))

    def increment_score(self):
        self.score += 1
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_new_high_score(self.score)
        self.score = 0
        self.write_score()

    def get_high_score(self):
        with open("data.txt", "r") as file:
            return int(file.read())
        
    def write_new_high_score(self, new_highscore):
        with open("data.txt", "w") as file:
            file.write(str(new_highscore))

    def write_game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("Game Over", align="center", font=("Verdana", 69, "normal"))
        self.color("white")
        self.goto(0,-30)
        self.write("Press Space to Continue", align="Center", font=("Verdana", 18, "normal"))
        self.goto(0,265)