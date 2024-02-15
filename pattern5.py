#pattern printing
n=1
l=int(input("enter no of lines"))
for i in range(1, l+1):
    for j in range(1, i + 1):
        print(n, end=" ")
        n=n+1
    print()
