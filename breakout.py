from tkinter import *
from turtle import Screen
from paddle import Paddle
from blocks import Blocks
from ball import Ball

# creating paddle
paddle= Paddle(0,-300)
# creating ball
ball=Ball()

# creating blocks
tens_points_blocks=[]
ten_points_blocks1=Blocks(-400,80)
tens_points_blocks.append(ten_points_blocks1)

twentys_points_blocks=[]
twenty_points_block1=Blocks(-400,150)
twentys_points_blocks.append(twenty_points_block1)

thirtys_points_blocks=[]
thirty_points_block1=Blocks(-400,220)
thirtys_points_blocks.append(thirty_points_block1)

# setting screen

screen=Screen()
screen.setup(width=900, height=600)
screen.bgcolor("Black")
screen.title("The Breakout game")
screen.tracer()
screen.listen()
screen.onkey(paddle.move_right,key="Right")
screen.onkey(paddle.move_left,key="Left")

# placing blocks
ten_new_xcor=-390


for num in range(1,18):
    if num % 2==0:
        ten_new_xcor+=100
        ten_points_blocks=Blocks(ten_new_xcor,80)
        tens_points_blocks.append(ten_points_blocks)


twenty_new_xcor=-390

for num in range(1,18):
    if num % 2==0:
        twenty_new_xcor+=100
        twenty_points_block=Blocks(twenty_new_xcor,150)
        twentys_points_blocks.append(twenty_points_block)

thirty_new_xcor=-390
for num in range(1,18):
    if num % 2==0:
        thirty_new_xcor+=100
        thirty_points_block=Blocks(thirty_new_xcor,220)
        thirtys_points_blocks.append(thirty_points_block)


game_is_on=True
while game_is_on:
    screen.update()
    ball.move()
    # detecting collision with borders
    if ball.xcor() > 430 or ball.xcor() < -430:
        ball.bounce_x()
    if ball.ycor() > 280:
        ball.bounce_y()
    if ball.distance(paddle) < 70 and ball.ycor() < -240:
        ball.bounce_y()
    blocks_left=False

    for blocks in tens_points_blocks:
     if ball.distance(blocks)< 70 and ball.ycor()<80 and blocks in tens_points_blocks:
        blocks.hide()
        ball.bounce_y()

    for blocks in twentys_points_blocks:
        if ball.distance(blocks) < 70 and ball.ycor() < 150 and blocks in twentys_points_blocks:
            blocks.hide()
            ball.bounce_y()

    for blocks in thirtys_points_blocks:
        if ball.distance(blocks) < 70 and ball.ycor() < 220 and blocks in thirtys_points_blocks:
            blocks.hide()
            ball.bounce_y()

screen.exitonclick()