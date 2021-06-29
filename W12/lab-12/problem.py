def flashcard(prompt,expected_answer):
    cards = {}
    cards[prompt]= expected_answer
    question='What is the capital of',prompt,'?'
    expected_answer = cards[prompt]
    answer = input(question)
    if answer.lower() == expected_answer.lower():
        print("Correct!")
    else:
        print("Sorry, that is wrong....")


flashcard('Wyoming','Cheyenne')
flashcard('Arkansas','littlerock')
flashcard('Montana','helena')
flashcard('NorthDakota','bismarck')





    