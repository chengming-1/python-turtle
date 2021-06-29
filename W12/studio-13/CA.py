import random

while True:
    name = input("What is your full name?") 
    print ("Hello " + name, "welcome to Ally")
    answer1=['good','not bad','cool','fine']
    answer2=['bad','not good','sad']
    prompt=input("how's going today? Good or bad?")
    if (prompt.lower() in answer1):
        options=["What things make you felling great?","Do you get lucky today?", "I bet you're OK"]
        output = random.choice(options)
        rand_num = random.randint(1,3)
        if (rand_num == 1):
            print("What things make you felling great?")
        elif (rand_num == 2):
            print("Do you get lucky today?")
        else:
            print("I bet you're OK")
        prompt2=input("Sounds good,")
    if (prompt.lower() in answer2):
        options=["why you felling sad?","What’s the matter?","You look under the weather today"]
        output = random.choice(options)
        rand_num = random.randint(1,3)
        if (rand_num == 1):
            print("why you felling sad?")
        elif (rand_num == 2):
            print("What’s the matter?")
        else:
            print("You look under the weather today")
    if (prompt.lower() not in answer1 or answer2):
        print("I dont sure what the emotion is")
    if (prompt.lower() == "goodbye" or "bye"):
        print("Have a nice day")
        break