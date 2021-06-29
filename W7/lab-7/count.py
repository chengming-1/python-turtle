

words = {}       # Create a blank dictionary to hold our counts

# Initialize the dictionary to 0 for all of the words



phrase =''' ‘Cause the players gonna play , play , play , play , play
And the haters gonna hate , hate , hate , hate , hate
Baby , I’m just gonna shake , shake , shake , shake , shake
I shake it off , I shake it off
Heartbreakers gonna break , break , break , break , break
And the fakers gonna fake , fake , fake , fake , fake
Baby, I’m just gonna shake , shake , shake , shake , shake
I shake it off , I shake it off
I shake it off , I shake it off
I , I shake it off , I shake it off
I , I shake it off , I shake it off
I , I shake it off , I shake it off'''

for letter in phrase.split():
        if letter not in words:
            words[letter] = 0
        if letter in words:
            words[letter] +=1
print(words)

