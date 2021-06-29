


words = {}       # Create a blank dictionary to hold our counts

# Initialize the dictionary to 0 for all of the words
words.setdefault('Baby',0)
words.setdefault('Im',0)
words.setdefault('just',0)
words.setdefault('gonna',0)
words.setdefault('shake',0)

phrase = "Baby, Im just gonna shake, shake, shake, shake, shake"

words['Baby'] += 1
words['Im'] += 1
words['just'] += 1
words['gonna'] += 1
words['shake'] += 5

for letter in phrase:
    print(letter)

print(words)
