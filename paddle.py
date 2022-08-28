from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,x_posi,y_posi):
        super().__init__()
        self.shape("square")
        self.color("White")
        self.penup()
        self.shapesize(stretch_wid=3, stretch_len=6)
        self.goto(x_posi,y_posi)

    def move_right(self):
        new_xcor=self.xcor()+50
        self.goto(new_xcor,-300)

    def move_left(self):
        new_xcor=self.xcor()-50
        self.goto(new_xcor,-300)

