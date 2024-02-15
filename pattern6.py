#pattern printing
n=1
l=int(input("enter no of lines"))
for i in range(l, 0,-1):
    for j in range(1, i + 1):
        print(n, end=" ")
    n+=1
    print()
