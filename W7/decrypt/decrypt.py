phrase = """
hnronxttfao  bphnbiifra.
"""

letter_count = {}
pool={"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}

for letter in phrase:
  if letter in letter_count:
    letter_count[letter] += 1
  else:
    letter_count[letter] = 1

while True:
  print(letter_count)
  print()
  print(phrase)
  print()
  
  replace=input("words to replace:")
  if replace == None:
    break
  for letter in pool:
      phrase = phrase.replace(letter_to_rep,letter)
      print(phrase)