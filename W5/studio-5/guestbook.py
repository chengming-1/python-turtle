from turtle import *

names=[]
penup()
left(90)
forward(300)
left(90)
forward(300)
pendown()
write("Please enter your full name,enter ""end"" to show the whole guestbook", font=("Helvetica", 10, "italic"))
penup()
left(90)
forward(60)
pendown()

while True:   
    penup()
    forward(20)
    pendown()
    newname = textinput("Name", "Please enter your name")
    message = textinput("Message","any message")
    
    group= newname+":"+message  
    if newname !="end":
        write(group,font=("Helvetica", 10, "italic"))
        names.append(newname)
        names.sort()
    if newname == "end" or message == "end" or newname==None or message==None:
        penup()      
        forward(40)
        pendown()
        write("guest List:",font=("Helvetica", 20, "italic"))
        penup()      
        forward(60)
        write(names,font=("Helvetica", 12, "italic"))
        forward(20)
        pendown()
        break
done()