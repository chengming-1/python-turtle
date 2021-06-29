# Purpose: 

def letter_places(str, letter):                           # define the function to find the letter in the stream
    places = []                                           #define the function to check the number of the letter
    start = 0                                            # make sure the program star from the very first of the message.
    while True:                                          # keep running the loop
        where = str.find(letter,start)                   # give a signal when the program find a letter
        if (where == -1):                                # if the don't have the same letter
            break                                        # stop the loop
        places.append(where)                             # stay there
        start = where + 1                                # give the answer 0
    return places                                        # goes back to the beginning of the program

def nth(num):                                           
    if num == 1:
        return str(num) + "st"
    if num == 2:
        return str(num) + "nd"
    if num == 3:
        return str(num) + "rd"
    return str(num) + "th"

user_input = input("Enter a message: ")
user_letter = input("What letter are you looking for? ")

places = letter_places(user_input, user_letter)

if len(places) == 0:
    print("That letter does not appear")
else:
    for place in places:
        print("That letter is the", nth(place+1), "letter")





