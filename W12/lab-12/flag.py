from turtle import *

def stripe(col,length,width):
    if col == 'red' or col =='white':
        color(col)
        begin_fill()
        forward(length)
        left(90)
        forward(width)
        left(90)
        forward(length)
        left(90)
        forward(width)
        left(90)
        end_fill()
        penup()
        right(90)
        forward(10)
        left(90)
        pendown()
    elif col =='blue':
        penup()
        goto(0, -60)
        pendown()
        color("blue")
        begin_fill()
        forward(length)
        left(90)
        forward(width)
        left(90)
        forward(length)
        left(90)
        forward(width)
        left(90)
        end_fill()
    else:
        print('undefined color.')


def move_next():
    penup()
    right(90)
    forward(10)
    left(90)
    pendown()

def blue_box():
    color("blue")
    begin_fill()
    forward(100)
    left(90)
    forward(70)
    left(90)
    forward(100)
    left(90)
    forward(70)
    left(90)
    end_fill()

  
