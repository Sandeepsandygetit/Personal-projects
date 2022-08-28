from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("White")
        self.goto(0,-280)
        self.x_move=20
        self.y_move=20

    def move(self):
        new_xcor=self.xcor() +self.x_move
        new_ycor=self.ycor() +self.y_move
        self.goto(new_xcor,new_ycor)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1