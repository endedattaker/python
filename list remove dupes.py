#remove dupes
list1=[]
limit=int(input("enter limit"))
for i in range(limit):
  no=int(input("enter number"))
  list1.append(no)
print(list1)
result=[]
for i in list1:
  if i not in result:
    result.append(i)
print(result)
