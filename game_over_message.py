from turtle import Turtle

class GameOverMessage(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.hideturtle()
        self.color("red") 
        self.write(f"Game Over", align="center", font=("Verdana", 30, "normal"))
        