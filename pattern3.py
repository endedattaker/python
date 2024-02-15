#pattern printing
l=int(input("enter no of lines"))
for i in range(l, 0,-1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
