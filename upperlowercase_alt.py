a="python oops"
l=len(a)
for i in range(0,l):
  if i%2==0:
    print(a[i].upper(),end="")
  else:
    print(a[i].lower(),end="")
