from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, player):
        super().__init__()
        self.positions = [(-350, 0), (350, -20)]
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_len=5, stretch_wid=1)
        if player == 'left':
            self.goto(self.positions[0])
        elif player == 'right':
            self.goto(self.positions[1])

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)


