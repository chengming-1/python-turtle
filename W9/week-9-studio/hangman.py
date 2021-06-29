from turtle import *
import random 
def word():
    words=['try',
           'hard',
           'hangman',
           'information']
    return random.choice(words)
        
def compared(goal, guesses,user_input):
    user_input=user_input.lower()
    matches=0
    process=''
    for letter in goal:
        if letter in guesses:
            process += letter
        else:
            process +="_"
        if letter == guesses:
            matches += 1
    if matches > 1:
        print("The word contains", matches,"of",user_input,"s")
    elif matches == 1:
        print("The word contains the letter,",user_input)
    else:
        print("Sorry, the letter is not in the word.")
    return process

    
def main():
    goal=word()
    guesses=[]
    guessed= False
    times= 0
    print("the word contains",len(goal), "letters")
    while not guessed:
        user_input=input("enter a letter:") 
        if user_input in guesses:
            print("Congratulations! You got it!")
        elif len(user_input)==1:
            guesses.append(user_input)
            result = compared(goal,guesses,user_input)
            times +=1
            if result ==goal:
                guesses = True
            else:
                print(result)
        elif len(user_input)>1 and user_input != goal:
            print("Invalid input.")
    
        
main()
        