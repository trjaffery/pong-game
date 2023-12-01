from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.goto(0,0)
        self.penup()
        self.color("blue")
        self.x_move = 3
        self.y_move = 3

    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)


    def refresh(self):
        self.goto(0,0)

    def bounce(self):
        self.y_move *= -1


    def paddle_bounce(self):
        self.x_move *= -1

