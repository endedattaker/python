#pattern printing
l=int(input("enter no of lines"))
for i in range(1, l+1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
for i in range(l-1, 0,-1):
    for j in range(1, i + 1):
        print(j, end=" ")
    
    print()
