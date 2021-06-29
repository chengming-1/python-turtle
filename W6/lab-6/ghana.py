from turtle import *

### Functions for drawing

def bar(bar_color):
    fillcolor(bar_color)
    begin_fill()
    forward(300)
    right(90)
    forward(50)
    right(90)
    forward(300)
    right(90)
    forward(50)
    right(90)
    end_fill()

def star():
    for i in range(5):
        fillcolor("black")
        begin_fill()
        forward(20)
        right(144)
        end_fill()
        forward(25)
def star(size):
    for i in range(5):
        forward(size)
        right(144)
    
### Main code that gets run, to draw the german flag

bar("red")
right(90); forward(50); left(90)
bar("yellow")
right(90); forward(50); left(90)
bar("green")
forward(130)
penup()
left(72)
forward(0)
pendown()
fillcolor("black")
begin_fill()
star(52)
end_fill()



done()

    
