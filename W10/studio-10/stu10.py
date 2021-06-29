import random
def ask(questions):
    print(questions.keys())
    answer=input("Your answer:")
    if answer == questions.values():
        print("Right!")
    else:
        print("Sorry, Thats wrong")
  
q1={"How many multiples does 25 have?":"2"}
q2={"How many prime numbers are between 1 and 20?":"8"}
q3={"((6*8)+2)/10":"5"}
q4={"(6^2)^2)":"1296"}
q5={"If  a dozen eggs are 12 cents how many eggs can you get with one dollar?":"96"}
q6={"sqr(144)":"12"}
q7={"4^5":"1024"}
q8={" What is the 6th number of the Fibonacci Sequence?":"8"}
q9={"(4*5/2)+15/5":"5"}
q10={"What is the derivative of x^3 /2 + x^2 /5 + 7 ?":"3x^2/2+2x/5"}
questions=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]

ask(random.choice(questions))