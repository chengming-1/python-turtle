import random
#morse code
code = { 'A':'.-', 'B':'-...',
        'C':'-.-.', 'D':'-..', 'E':'.',
        'F':'..-.', 'G':'--.', 'H':'....',
        'I':'..', 'J':'.---', 'K':'-.-',
        'L':'.-..', 'M':'--', 'N':'-.',
        'O':'---', 'P':'.--.', 'Q':'--.-',
        'R':'.-.', 'S':'...', 'T':'-',
        'U':'..-', 'V':'...-', 'W':'.--',
        'X':'-..-', 'Y':'-.--', 'Z':'--..',
        '1':'.----', '2':'..---', '3':'...--',
        '4':'....-', '5':'.....', '6':'-....',
        '7':'--...', '8':'---..', '9':'----.',
        '0':'-----'}

questions=list(code)
#checking and answer function
def checker(question,answer):
    if code[question]==answer:
        return True
    else:
        return False



#display function
def display(question,answer,correct):
    print("The choice you got was:",question)
    print("The answer you gave is:",answer)
    if correct==False:
        print("Your answer is false.")
    if correct==True:
        print("Your answer is true.")
        



#main program
print("Welcome to the Morse Code Flashcards!!!!")
print("A random choice of a letter or number will be given and you will provide an answer.")
print("Good Luck")
print()
for count in range(10):
    question=random.choice(questions)
    print("The chosen item is: ",question)
    answer=input("Please enter the morse code translation of this letter or number:\n")
    print()
    answer=answer.replace(" ","")
    result=checker(question,answer)
    #display
    display(question,answer,result)
    print()
    del questions[questions.index(question)]
    del code[question]