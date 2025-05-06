from turtle import Turtle
ALIGNMENT = 'left'
CENTER = ('Arial', 12, 'normal')


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.level = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.level}", move=False, align=ALIGNMENT, font=CENTER)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=CENTER)


    
    