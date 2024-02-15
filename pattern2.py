#pattern printing
l=int(input("enter no of lines"))
for i in range(1, l+1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
