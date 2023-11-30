from turtle import Turtle, Screen
from background_setup import Background


# TODO: #1 - Create the screen

screen = Screen()
screen.bgcolor("black")
screen.setup(1200, 800)

background = Background()

background.create_line()
background.score()

# TODO: #2 - Create and move a paddle

# TODO: #3 - Create another paddle

# TODO: #4 - Create the ball and make it move

# TODO: #5 - Detect collision with wall and bounce

# TODO: #6 - Detect collision with paddle

# TODO: #7 - Detect when paddle misses

# TODO: #8 - Keep Score


screen.exitonclick()
