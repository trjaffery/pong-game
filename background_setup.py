from turtle import Turtle


class Background(Turtle):

    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.speed("fastest")
        self.hideturtle()
        self.color("white")
        self.penup()

    def create_line(self):
        self.goto(x=0, y=400)
        self.setheading(270)
        for num in range(0, 20):
            self.penup()
            self.forward(20)
            self.pendown()
            self.forward(20)

    def score(self, position):
        self.color("white")
        self.penup()
        self.goto(position)
        self.write(self.score1, align="center", font=('courier', 40, 'normal'))

    def increase_score(self, player):
        self.score1 += 1

    def game_over(self):
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=('courier', 20, 'normal'))
