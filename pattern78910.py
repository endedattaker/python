#pattern print
l=5
for i in range(1,l+1):
  for j in range(1, i+1):
    print(j*2, end=" ")
  print()

#pattern print
rows = 6
for i in range(1, rows):
   
    for j in range(rows, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print(j, end=' ')
            
    print("")

#pattern print
l=5
for i in range(1,l+1):
  for j in range(1, i+1):
    if j%2==0:
      print("+", end=" ")
    else:
      print("*",end=" ")
  print()

#pattern print
p= 5
for i in range(p, 0, -1):
    for j in range(1, i + 1):
        print(j,end=' ' )
    print()
l=6
for i in range(2,l):
  for j in range(1, i+1):
    print(j, end=" ")
  print()
