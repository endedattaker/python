l=int(input("enter limit:"))
c=0
n1=0
n2=1
if l<=0:
  print("Please enter a positive integer")
elif l==1:
  print(n1)
else:
  while c<l:
    print(n1)
    n3=n1+n2
    n1=n2
    n2=n3
    c=c+1
