from turtle import Turtle


class Background(Turtle):

    def __init__(self):
        super().__init__()
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

    def game_over(self):
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=('courier', 20, 'normal'))


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_right = 0
        self.score_left = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-60, 230)
        self.write(self.score_left, align="center", font=('courier', 40, 'normal'))
        self.goto(60, 230)
        self.write(self.score_right, align="center", font=('courier', 40, 'normal'))

    def left_point(self):
        self.score_left += 1
        self.update_scoreboard()

    def right_point(self):
        self.score_right += 1
        self.update_scoreboard()
