# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 16:27:28 2020

@author: 73251
"""

print("After centuries they're back. The demons have returned, the seal is weakened. And once more these ancient creatures are roaming the world and infesting the lands.")
print("Their shadow has spread across the Kingdom of Gantrick, and now the said kingdom has completely fallen under their influence.")
print("You're Trinog Dragonhold, from a child with past of mystery, to a king of city of Ergas and Skyguard Empire. But not all of your mysteries have been resolved, the truth waits to be found.")
print("News of this are fast in reaching you, and the news have forced you to act in desperate attempt to convince the stubborn people of Dragonguard to evacuate the city.")
print("Before you proceed, allow me to ask you a question or two..")
choice_1=input("During Equia, Artifacts of Zazkor..you've had a choice to romance someone.Estrella or Lilian. Do remind me who was it?")


if (choice_1 == "estrella") or (choice_1 == "Estrella"):
    print("Alrighty!")
    print("You're proud owner of the city of Ergas, and King of Skyguard Empire. During Equia Artifacts of Zazkor, there were multiple chances to obtain and/or upgrade your new city.")
    choice_2 = input("Nonsense, you're a wise and cunning ruler my lord! You think that right?")
    
    if (choice_2 == "yes") or (choice_2 == "Yes"):
        print("Winds are blowing…giving haste to your sailing speed..as if gift by gods..only that you not so long ago learned there are none.")
        print("As you're sitting within your cabin a knocking sound is heard.")
        print("Estrella tilts her head slowly, smiling towards you, listening.")
        choice_3 = input("You look great, are you planning to charm the demons?")
        if (choice_3 == "yes") or (choice_3 == "Yes"):
            print("Oh if i could i would, but that is a doubtful strategy.She grins.")
            print("Estrella goes quiet, but she is really annoyed at the moment. And last time you saw Estrella that annoyed, she chopped a head off.")
        else:
            print("You Dead!")
    else:
        print("You Dead!")
    
elif choice_1.lower() == "lilian":
    print("Alrighty!")
    print("You're proud owner of the city of Ergas, and King of Skyguard Empire. During Equia Artifacts of Zazkor, there were multiple chances to obtain and/or upgrade your new city.")
    choice_4 = input("Nonsense, you're a wise and cunning ruler my lord! You think that right?")   
    if (choice_4 == "yes") or (choice_4 == "Yes"):
        print("Winds are blowing…giving haste to your sailing speed..as if gift by gods..only that you not so long ago learned there are none.")
        print("The rest of the ships are behind you and are bringing Ergas military with you. For whatever good that will do, but you did not take everyone no. You're well aware you can not match up demons in fair fight, there are only so much to help you evacuate the city and supplies, the rest of space is reserved for people of Dragonguard.As you're sitting within your cabin a knocking sound is heard.")
        print("Lilian tilts her head slowly, smiling towards you, listening.")
        print("I know you're nervous, i am not any better. But please…promise me you wont do something reckless again. No, matter of fact i will not allow it. She says firmly, glaring at you.")
        choice_5 = input("Trinog.She smiles towards you somewhat.Continue?")
        if (choice_5 == "yes") or (choice_5 == "Yes"):
            print("She pulled out a knife and stabbed it straight up")
            print("You Dead")
        else:
            print("Trinog, i swear to gods..i will knock you out myself if you dare to attempt something like that and drag you back myself.")
            print("Estrella sits down on the bed and next to you, her arms slowly wrap around you and she lands a soft kiss on your cheek.You're cute..She says, smiling warmly at you....")
else:
    print("cant choose this person")