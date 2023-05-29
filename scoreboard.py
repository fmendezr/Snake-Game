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