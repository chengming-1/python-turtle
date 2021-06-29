
# Main code that counts letters in a string
input_string=""
def count_letters(input_string):
    letters = {}
    for letter in input_string:
        letters.setdefault(letter, 0)
        letters[letter] += 1
    print(letters)
    return letters
        

# Code to test the count_letters function
count_letters(input_string)