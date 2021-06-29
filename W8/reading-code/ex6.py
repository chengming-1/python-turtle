# Purpose:         #to pick up random numbers and letters to comby as a password

import random        # use the python function of random

def random_letter():                # define random letter from a branch of them
    letters = 'abcdefghijklmnopqrstuvwxyz'   #give the range of letters from "a" to "z"
    letters = letters + letters.upper()    # to add the captial letters to the range
    return random.choice(letters)            #pick up random letters from the range

def random_number():                # define random number from a branch of them
    numbers = '0123456789'             # give the range of random number from "0" to "9"
    return random.choice(numbers)      #pick up number from the range

howlong = input("How long do you want it to be? ") # ask how long user want it to be
out = ""                                         # input a number

for char in range(int(howlong)):                   # to make sure the longth gose to be a integrat number
    which = random.choice(["letter", "number"])    # random pick up letters or numbers 
    if which == "letter":                           #if it is the letter gose 
        out = out + random_letter()
    else:
        out = out + random_number()

print(out)
