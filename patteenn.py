l=11

for i in range(1,l+1):
  if i%2==1:
    for j in range(1,i+1):
       print(2 * j - 1, end="")
       if j < i:
        print("  ", end="")
  else:
    for j in range(1,i+1):
       print(2 * j, end="")
       if j < i:
        print("  ", end="")
  print()