import sys
import pprint
input_filename = sys.argv[1]
output_filename = sys.argv[2]
with open(input_filename,"r") as f:
    count=0
    words = {}
    for line in f:
        line=line.split()
        count+=len(line)
    for letter in f:
        letter=letter.split()
        if letter not in words:
            words[letter] = 0
        if letter in words:
            words[letter] +=1
    pprint.pprint(count)
    p=open(output_filename,"w")
    p.write(str(count))
    p.write(str(words))
    p.close()
    
