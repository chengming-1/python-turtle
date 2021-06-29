# Purpose: input some message and count the common letter and word

def get_input():#define a function to input message
    print("Please enter some text...")      #print out to let user know what to do next
    user_input = ""                         #collect all input
    while True:                             #keep loop
        new_input = input(">>> ")           #get the input
        if new_input == "":                 #if there's nothing
            break                           #stop the loop
        user_input = user_input + "\n" + new_input #add new input
    return user_input                       #back to begin

def count_lines(str):                       #def function to count lines
    return len(str.split("\n"))             #count the lens of input

def count_words(str):                       #def a function to count word
    words = {}                              #make a dictionary of words
    str = str.replace("\n", " ")            #remove all the space
    str = str.replace(",", " ")             #remove all comma
    str = str.replace(".", " ")             #remove all period
    str_words = str.split()                 #split the words
    for word in str_words:                  #set the word in the message  
        words.setdefault(word, 0)           #join the dictionary
        words[word] = words[word] + 1       #count the number appears
    return words                            #back to begin

def count_letters(str):                     #define function with the string to count letters
    all_letters = "abcdefghijklmmopqrstuvwxyz" #all letter sets
    letters = {}                                #create a dictionary of letters
    for letter in str.lower():                  #count the letter in strings
        if letter in all_letters:               #check it's a letter
            letters.setdefault(letter, 0)       #make the letter into dictionary
            letters[letter] = letters[letter] + 1#count when appeared
    return letters                                  #back to loop

def dict_max(d):#define a function to show the number of list
    max_key = None#set no limit at the beginning
    max_value = 0#set no count at begining
    for key in d.keys(): #check with input
        if d[key] > max_value: #compared counts
            max_key = key #increase to the higher one
            max_value = d[key]#increase to the higher one
    return max_key #back to begining


user_input = get_input()#ask for input
print("Number of lines: ", count_lines(user_input))#print out the lines
print("Most Common word: ", dict_max(count_words(user_input)))#print out the most word 
print("Most Common letter: ", dict_max(count_letters(user_input)))#print out the most letter
