
# Create an empty dictionary
names = {}


names['Wash'] = 'Rick'
names['Geier'] = 'Caitlin'
names['DiLisio'] = 'Armand'
names['wang']='chengming'

a = input("Enter the last name of a student: ")
b = input("Enter the First name of a student: ")
names[a]=b

while True:
    last_name = input("Enter a student's last name: ")
    if last_name in names:
        print("Their first name is", names[last_name])
    if last_name not in names:
        print("I dont know that student")
    if last_name == "":
        # If the user hits enter without entering a name, stop the loop
        break
