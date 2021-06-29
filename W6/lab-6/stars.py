from turtle import *
import random as random

### Functions

def star(length):
    for i in range(5):
        forward(length)
        right(144)
        end_fill()
        forward(25)

### The main code that gets run


for i in range(13):
    star(random.randrange(10,40))
    penup()
    right(360/13)
    forward(80)
    pendown()

done()
