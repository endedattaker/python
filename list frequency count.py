#frequency count
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
for j in result:
  c=0
  for k in list1:
    if j==k:
      c=c+1
  print(j,"occured",c,"times")
