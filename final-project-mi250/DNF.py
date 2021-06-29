#Dungeon and Fighter -- an Adventure program
import sys
import turtle
from turtle import *
from logo import *
print("You have come as a warrior to a place called land arad. A young gril beside you named 'Celia' looks at you in surprise, but moments later she calms down and says to you:")
print("")
Answer = input("are you the brave one who prophesied to save us? 'Yes or No':")

if (Answer == "Yes") or (Answer =="yes"):
      for line in open("begin.txt",'r'):
        line = f.readlines()
        print(line.replace('\n',''))
    number = input("pick a number '1-6':")


  if (number == "1"):
    print("The monsters here are too strong for you to handle. But luckily you survived. Celia no longer thinks of you as a warrior. 'normal end'")

  elif (number == "2"):
    print("The monsters here are too strong for you to handle. But luckily you survived. Celia no longer thinks of you as a warrior. 'normal end'")

  elif (number == "3"):
  	print("The monster here is too strong, you are directly killed seconds. 'bad end'")

  elif (number == "4"):
    print("You can not go into the Mysterious world. Maybe when you get stronger you can find a way in.'back to the previous step'")

  elif (number == "5"):
      for line in open("begin.txt",'r'):
        line = f.readlines()
        print(line.replace('\n',''))
        place1 = input("pick a number '1-4':")

  if (place1 == "1"):
      for line in open("The Castle in The Sky.txt",'r'):
        line = f.readlines()
        print(line.replace('\n',''))
      place2 = input("pick a number '1-3':")

      if (place2 == "1"):
      for line in open("West Coast 1.txt",'r'):
        line = f.readlines()
        print(line.replace('\n',''))
        place3 = input("pick a number '1-2':")

        if (place3 == "1"):
          print("You were torn by the portal.")

        elif (place3 == "2"):
            for line in open("Mysterious World2.txt",'r'):
                line = f.readlines()
                print(line.replace('\n',''))
          choice = input("pick a number '1-2':")

          if (choice == "1"):
            print("Celia was saved, but you lost the opportunity to enter the mysterious land, the world is temporarily safe, but one day evil will come to this world again, and at that time no one can save this world ...........")
            screen = turtle.Screen()
            image = "1.gif"
            screen.addshape(image)
            turtle.shape(image)

        elif (choice == "2"):
            logo()
            print("The devil is destroyed and the world is safe. People are cheering, triumphant, and you cried while holding Celia's body .......")

      elif (place2 == "2"):
        print("The monsters here are too strong for you to handle.  But luckily you survived. Celia no longer thinks of you as a warrior. ")
      elif (place2 == "3"):
        print("You can't go into the Mysterious world. Maybe when you get stronger you can find a way in.")

    elif (place1 == "2"):
      print("The monsters here are too strong for you to handle.  But luckily you survived. Celia no longer thinks of you as a warrior. 'normal end'")
    elif (place1 == "3"):
      print("The monsters here are too strong for you to handle.  But luckily you survived. Celia no longer thinks of you as a warrior. 'normal end'")
    elif (place1 == "4"):
      print("You were torn by the portal.")
  elif (number == "6"):
    print("You chose to look at the sheepskin book. It says: 'to save the world you must do what you can, o great brave man, cross Land of life to bird cities, reach busy ports, enter powerful empires, and finally find the portal. Enter the lost land. Don't get lost, don't try any non-existent behavior, I believe you will be our warrior!' ")

  else:
  	print("You lost control and killed the girl in front of you. The world has lost the only chance to be saved, but at the same time your actions attract evil attention, and eventually, you become the demon king of this world. 'Mysterious ending'")

elif (Answer == "No") or (Answer == "no"):
  print("Celia did not bother you can left. you have lived an ordinary life.")
elif (Answer =="quit"):
    sys.exit()
