from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        
        self.penup()
        self.x=10
        self.y=10
        self.movespeed=0.1
    def move(self):
        x=self.xcor()+self.x
        y=self.ycor()+self.y
        self.goto(x,y)
    def bounce(self):
        self.y*=-1
    def bouncep(self):
        self.x*=-1
        self.movespeed*=0.9
    def reset(self):
        self.goto(0,0)
        self.movespeed=0.1
        self.bouncep()
        
        
