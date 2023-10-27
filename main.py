from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.bgcolor("Black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)
scoreboard=Scoreboard()

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))

ball=Ball()





screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_is_on=True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()



    #detect collision

    if ball.ycor()>280 or ball.ycor()<-280:
        #needts to bounce
        ball.bounce_y()

    if ball.distance(r_paddle)<50 and ball.xcor()>340 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
       ball.bounce_x()

    #detect r paddle missed

    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()

    #detect l paddle missed
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()
screen.exitonclick()