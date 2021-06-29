beer=[]
for i in range(99,-1,-1):
    beer.append(i)
    if i > 6:
        print(str(i)+ "bottles of beer on the wall")
        print(str(i)+ "bottles of beer")
        print("Take one down, pass it around")
    elif i == 0:
        print("No more bottles of beer on the wall, no more bottles of beer. We've taken them down and passed them around; now we're drunk and passed out!")
        
    elif i == 6 :
        i=int(i)
        print("If one of those bottles should happen to fall,")
        print(int(i)-1, "bottles of beer on the wall")
        print(int(i)-1, "bottles of beer")
        print("Take one down, pass it around")
    elif i< 6 and i>1:
        i=int(i)
        print(int(i)-1, "bottles of beer on the wall")
        print(int(i)-1, "bottles of beer")
        print("Take one down, pass it around")