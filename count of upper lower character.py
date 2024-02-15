#count of upper lower character
a=str(input("enter string:"))
l=len(a)
u=0
low=0
for i in range(0,l):
  if a[i]==a[i].upper():
    u=u+1
  else:
    low=low+1
print("upper count=",u)
    
print("lower count=",low)
