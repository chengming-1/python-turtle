import random

while True:
    number1= random.randint(1,150)
    number2= random.randint(1,150)
    print("question: what is", number1,"+",number2)
    result=int(input("answer 1:"))
    if result == number1 + number2:
        print("True")
        print("question: what is", number1,"-",number2)
        result2=int(input("answer 2:"))
        if result2 == number1-number2:
            print("True")
            break
        else:
            print("False,try again")
    else:
        print("False,try again")
        
        
        
        