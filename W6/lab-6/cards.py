from turtle import *

#####  Functions that draw card shapes

def diamond():
    fillcolor("red")
    begin_fill()
    setheading(90)
    left(30)
    forward(50)
    right(60)
    forward(50)
    right(120)
    forward(50)
    right(60)
    forward(50)
    end_fill()
    setheading(0)

def heart():
    fillcolor("red")
    begin_fill()
    setheading(90)
    right(30)
    forward(72)
    left(30)
    circle(18, 180)
    left(180)
    circle(18, 180)
    left(30)
    forward(72)
    end_fill()
    setheading(0)

def club():
    fillcolor("black")
    begin_fill()
    setheading(0)
    forward(8)
    left(105)
    forward(30)
    left(150)
    forward(30)
    left(105)
    forward(8)
    end_fill()
    
    setheading(90)
    forward(50)
    right(90)
    begin_fill()
    circle(18)
    end_fill()
    begin_fill()
    left(120)
    circle(18)
    end_fill()
    begin_fill()
    left(120)
    circle(18)
    end_fill()
    setheading(270)
    forward(50)
    setheading(0)


def spade():
    setheading(0)
    begin_fill()
    forward(15)
    left(120)
    forward(30)
    left(120)
    forward(30)
    left(120)
    forward(15)
    end_fill()

    setheading(90)
    forward(25)
    left(180)
    left(45)
    begin_fill()
    circle(18,180)
    forward(36)
    left(90)
    forward(36)
    circle(18, 180)
    end_fill()
    left(45)
    back(25)
    setheading(0)

def move_next():
    penup()
    forward(70)
    pendown()

def selection(user):
    if user == 'diamond':
        diamond()
    elif user == 'heart':
        heart()
    elif user == 'club':
        club()
    elif user == 'spade':
        spade()
    move_next()

#### The main code that gets run
choices = []
for i in range(5):
    user = input('What card would you like to draw? (diamond, heart, club, or spade)')
    choices.append(user)
for i in range(5):
    selection(choices[i])

print("Come again")
done()
