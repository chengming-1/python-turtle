import random
restaurants = []
ask=int(input("how many restaurants: "))

for i in range(1,ask+1):
    place = input("Enter the name of restuarant " + str(i) + ": ")
    restaurants.append(place)

print(restaurants)
print("You should go to:",random.choice(restaurants))
