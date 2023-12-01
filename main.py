from turtle import Turtle, Screen
from background_setup import Background, Scoreboard
from paddle import Paddle
from ball import Ball
import time

# TODO: #1 - Create the screen

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

background = Background()

background.create_line()
screen.update()

# TODO: #2 - Create and move a paddle

paddle_left = Paddle('left')

# TODO: #3 - Create another paddle

paddle_right = Paddle('right')

# TODO: #4 - Create the ball and make it move

ball = Ball()

screen.listen()
screen.onkey(key='w', fun=paddle_left.move_up)
screen.onkey(key='s', fun=paddle_left.move_down)
screen.onkey(key='Up', fun=paddle_right.move_up)
screen.onkey(key='Down', fun=paddle_right.move_down)

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)

    ball.move()

    # TODO: #5 - Detect collision with wall and bounce

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # TODO: #7 - Detect when paddle misses
    # TODO: #8 - Keep Score

    if ball.xcor() > 380:
        scoreboard.left_point()
        ball.refresh()
        paddle_right.refresh()
        paddle_left.refresh()
    if ball.xcor() < -380:
        scoreboard.right_point()
        ball.refresh()
        paddle_right.refresh()
        paddle_left.refresh()

    # TODO: #6 - Detect collision with paddle

    if (ball.distance(paddle_right) < 50 and ball.xcor() > 320 and (0 <= ball.heading() <= 90
                                                                    or 270 <= ball.heading() <= 360)
            or ball.distance(paddle_left) < 50 and ball.xcor() < -320
            and 90 <= ball.heading() <= 270):
        ball.paddle_bounce()
        ball.increase_speed()

    if scoreboard.score_right == 7 or scoreboard.score_left == 7:
        background.game_over()
        game_is_on = False


screen.exitonclick()
