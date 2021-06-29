from turtle import *


name = textinput("Name", "Please enter your name")
right(90) 

while True:
    write(name)
    penup()
    forward(50)
    pendown()
    name = textinput("Name", "Please enter your name")
    

done()
