n= int(input("Enter the value of N: "))
s=0
for x in range (1,n+1):
    if n%x==0:
        s=s+x
print(s)
