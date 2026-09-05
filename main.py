from turtle import Screen,Turtle
from PADDLECLASS import Paddle
from balclass import Ball
from scoreclass import Scoreboard
import time
screen=Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.tracer(0)
screen.title('PONG')
r_paddle=Paddle((380,0))
l_paddle=Paddle((-380,0))
'''r_paddle.goto(380,r_paddle.xcor())
l_paddle.goto(-380,r_paddle.xcor())'''
ball=Ball()
score=Scoreboard()


'''def up():
    Y=paddle.ycor()+20
    paddle.goto(paddle.xcor(),Y)
def down():
    Y=paddle.ycor()-20
    paddle.goto(paddle.xcor(),Y)'''

gameon=True
screen.listen()
while gameon:
    time.sleep(ball.movespeed)
    screen.update()
    '''screen.onkey(up,'Up')
    screen.onkey(down,'Down')'''
    screen.onkeypress(r_paddle.up,'Up')
    screen.onkeypress(r_paddle.down,"Down")
    screen.onkeypress(l_paddle.up,'w')
    screen.onkeypress(l_paddle.down,'s')
    ball.move()
    ## for collision with wall
    if ball.ycor()>280 or ball.ycor()<-280 :
        ball.bounce()
    ## for collision with paddle
    Y=r_paddle.ycor()
    Y1=l_paddle.ycor()
    if ball.xcor()>360 and ball.ycor() in range(Y-50,Y+50)  or ball.xcor()<-360 and ball.ycor() in range(Y1-50,Y1+50) :
        ball.bouncep()
        time.sleep(ball.movespeed)
    ''' Y = r_paddle.ycor()
    Y1 = l_paddle.ycor()

    if (
        ball.xcor() > 350 and
        Y - 50 <= ball.ycor() <= Y + 50
    ) or (
        ball.xcor() < -350 and
        Y1 - 50 <= ball.ycor() <= Y1 + 50
    ): 
        ball.bouncep()
        time.sleep(ball.movespeed)'''
    if ball.xcor()>380:
        ball.reset()
        time.sleep(ball.movespeed)
        score.l_point()
    if ball.xcor()<-380:
        ball.reset()
        score.r_point()
        time.sleep(ball.movespeed)





screen.exitonclick()