n=int(input("Enter the value : "))
r=0
c=int(input("Enter the value to check start : "))
while n>0:
  r=n%10
  rev=r
  n=n//10
if rev==c:
  print("yes")
else:
  print("no")
