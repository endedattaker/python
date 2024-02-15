n=int(input("enter limit"))
s=0
for i in range(1,n+1):
    n=int(input())
    if n%2==0:
        s=s+i
print(s)
