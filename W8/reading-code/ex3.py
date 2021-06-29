#purpose:this program could draw a picture with red white and blue with stand settings

from turtle import *        #use turtlr to show as picture

def bar(bar_color):         #define a function with color and shape
    old_fill = fillcolor()  #reset the color 
    old_pen = pencolor()    #set the color of pen(moving track)
    color(bar_color)        #set the color as the varible
    begin_fill()            #begin draw
    forward(300)            #move forward to draw
    left(90)                #turn angle
    forward(10)             #move forward to draw
    left(90)                #turn angle
    forward(300)            #move forward to draw
    left(90)                #turn angle
    forward(10)             #move forward to draw
    left(90)                #turn angle
    end_fill()              # end to draw
    color(old_pen, old_fill)#colored picture

def box(box_color):         #define a different picture
    color(box_color)        #set the color
    begin_fill()            #begin to draw
    for i in range(4):      #set the loop times
        forward(70)         #move forward to draw
        right(90)           #turn angle
    end_fill()              #end to draw


def next():                 #define a loop to move the pen
    penup()                 #up pen to make no track
    right(90)               #turn angle
    forward(10)             #move forward
    left(90)                #turn angle
    pendown()               #down pen to continue make the track

speed(9)                    #set the speed of pen

for i in range(6):          #set the loop times
    bar("red")              #run bar function with red color
    next()                  #run next function to move the pen's position
    bar("white")            #run bar function with white color
    next()                  #run next function to move the pen's position
bar("red")                  #run bar function with red color
next()                      #run next function to move the pen's position

penup(); goto(0,11); pendown() # move the pen to pointed position
box("blue")                    #define box color as blue

done()                         #finish the program
