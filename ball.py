from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.goto(0,0)
        self.penup()
        self.color("blue")
        self.ball_speed = 2

    def move(self):
        # x_cor = self.xcor() + self.x_move
        # y_cor = self.ycor() + self.y_move
        # self.goto(x_cor, y_cor)
        if self.xcor() == 0:
            self.setheading(random.randint(-45, 45))
        self.forward(self.ball_speed)

    def refresh(self):
        if self.xcor() < 0:
            self.goto(0, 0)
            self.setheading(random.randint(-45, 45))
        elif self.xcor() > 0:
            self.goto(0, 0)
            self.setheading(random.randint(135, 225))
            self.forward(1)
        self.ball_speed = 2

    def increase_speed(self):
        self.ball_speed += 0.5

    def bounce_wall(self):
        self.setheading(360 - self.heading())

    def paddle_bounce(self):
        self.setheading(180 - self.heading())
