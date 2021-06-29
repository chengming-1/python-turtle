# Purpose: It help user to choose a restaurant and draw up.

import random            #import random function
from turtle import *     #import turtule function to draw

def star(size, star_color): #define a function to draw star
    old_color = fillcolor()  #set original color
    fillcolor(star_color)   #set the color
    begin_fill()            #begin to draw
    for i in range(5):      #set the loop times
        forward(size)       #move forward with the varible
        left(72)            #turn angle
        forward(size)       #move forward with the varible
        right(144)          #turn angle
    end_fill()              #end to draw
    fillcolor(old_color)    #reset the color

def get_restaurants():      #set a function to ask restaurants and add into a list
    restaurant_list = []    #set a list to store the list
    while True:             #keep looping
        rest = input("What is a restaurant you like? ") #ask user 
        if rest == "":                                  #if there are nothing
            return restaurant_list                      #go back to start
        restaurant_list.append(rest)                    #add all answer to list

def draw_list(restaurants, choice):                 #define a function to draw the list
    for rest in restaurants:                        # set the word
        write(rest, font=("Arial", 20, "normal"))   #set the word shape
        if rest == choice:                          #if it's the same  with random
            penup(); back(50); left(90); forward(25); right(90); pendown()
            star(20, "red")
            penup(); right(90); forward(25); left(90); forward(50); pendown()
        penup(); right(90); forward(50); left(90); pendown()        #draw



rest_list = get_restaurants() #run the function to get the list
rest_list.sort() #sequence the list
to_go_to = random.choice(rest_list) #randomly choose one 
draw_list(rest_list, to_go_to) #draw 

done()#finish the program

        
