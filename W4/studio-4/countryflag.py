from turtle import *
color('red','red')
begin_fill()
while True:
    forward(100)
    right(120)
    forward(100)
    right(60)
    forward(40)
    right(120)
    forward(60)
    if abs(pos()) < 1:
        break

end_fill()

penup()
forward(250)
pendown()
right(90)
forward(120)
right(90)
forward(410)
right(90)
forward(270)
right(90)
forward(410)
right(90)
forward(150)

done()
