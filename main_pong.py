from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.title("The Pong Game")
screen.setup(800, 600)
screen.bgcolor('black')

screen.tracer(0)

r_pad = Paddle((350, 0))
l_pad = Paddle((-350, 0))
screen.listen()

screen.onkey(r_pad.go_up, "Up")
screen.onkey(r_pad.go_down, "Down")
screen.onkey(l_pad.go_up,"w")
screen.onkey(l_pad.go_down, "a")
ball = Ball()
scoreboard=ScoreBoard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    ball.move()
    # detect collision between the ball and wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_by_wall()
    # detect collision between the ball and the paddle
    if ball.distance(r_pad)<50 and ball.xcor()>320 or  ball.distance(l_pad)<50 and ball.xcor()<-320 :
        ball.bounce_by_paddle()



    # detect when right paddle misses the ball
    if ball.xcor()>380:
        ball.reset_pos()
        scoreboard.l_point()
    # detect collison with the left paddle
    if ball.xcor()<-380:
        ball.reset_pos()
        scoreboard.r_point()


screen.exitonclick()
