from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.color("white") 
        self.penup()
        self.hideturtle()
        self.goto(0, 265)
        self.write_score()
    
    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Verdana", 25, "normal"))

    def increment_score(self):
        self.score += 1
        self.write_score()