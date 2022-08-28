from turtle import Turtle

class Blocks(Turtle):
    def __init__(self,x_posi,y_posi):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=3,stretch_len=4)
        self.color("White")
        self.goto(x_posi,y_posi)


    def hide(self):
        self.reset()


