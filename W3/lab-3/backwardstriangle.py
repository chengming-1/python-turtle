count= int(input("what size?"))
for num in range(0,count):
    for num2 in range(count,0,-1):
        if num2-1>num:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()
