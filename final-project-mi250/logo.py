from turtle import*


def gear(count, width, height):

    angle = 90-(180/count)

    for _ in range(count):
        forward(width)
        left(angle)
        forward(height)
        right(90)
        forward(width)
        right(90)
        forward(height)
        left(angle)

def move1():
    penup()
    right(90)
    forward(20)
    left(90)
    pendown()

def move2():
    penup()
    right(90)
    forward(10)
    left(90)
    pendown()

def move3():
    penup()
    left(180)
    forward(95)
    left(90)
    forward(75)
    left(90)
    pendown()

def move4():
    penup()
    right(35)
    forward(135)
    left(90)
    forward(135)
    right(180)
    pendown()

def star():
    color('darkred', 'gold')
    begin_fill()
    for i in range(33):
        forward(200)
        left(170)
    end_fill()

speed(0)


fillcolor("black")
begin_fill()
gear(36, 10, 10)
end_fill()
move1()
pencolor("brown")
fillcolor("sienna")
begin_fill()
gear(32, 9, 9)
end_fill()
move2()
pencolor("white")
fillcolor("silver")
begin_fill()
gear(28, 9, 9)
end_fill()
move3()
star()
move4()
pencolor("red")
write("DNF",font=("Arial",60,'normal','bold'))

done()
