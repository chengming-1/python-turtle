import sys
from operator import itemgetter
from turtle import *

def wordlist(filename):
    try:
        with open(filename,"r") as f:
            content = f.read()
    except FileNotFoundError:
        print("The file " + filename + " does not exist.")
    else:
        content = content.replace(',', ' ')
        content = content.replace('.', ' ')
        content = content.replace('!', ' ')
        content = content.replace(';', ' ')
        content = content.replace('?', ' ')
        content = content.strip()
        words = [word.lower() for word in content.split()]
        return words

    
def count_results(filename):
    wordscount = {}
    words = wordlist(filename)
    wordscount = wordscount.fromkeys(words)
    for word in wordscount.keys():
        number = words.count(word)
        wordscount[word] = number
    wordscount = sorted(wordscount.items(), key=itemgetter(1), reverse=True)
    return wordscount
 
    
def draw():
    penup()
    left(90)
    forward(300)
    left(90)
    forward(300)
    pendown()
    for word, wordcount in wordscount[:2]:
        penup()
        left(90)
        forward(60)
        pendown()
        write(word,font=("Helvetica", 20, "italic"))
    for word, wordcount in wordscount[3:5]:
        penup()
        forward(60)
        pendown()
        write(word,font=("Helvetica", 15, "italic"))
    for word, wordcount in wordscount[6:10]:
        penup()
        forward(40)
        pendown()
        write(word,font=("Helvetica", 12, "italic"))

    

filename = sys.argv[1]
wordscount=count_results(filename)
draw()

