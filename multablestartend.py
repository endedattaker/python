s=int(input("Enter start range : "))
r=int(input("Enter end range : "))
for i in range(s,r+1):
  for j in range(s,11):
    print(i,"*",j,"=",i*j)
  print("")
