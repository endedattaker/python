#second largest element in a list
list1=[]
limit=int(input("enter limit"))
for i in range(limit):
  no=int(input("enter number"))
  list1.append(no)
print(list1)
lar=list1[0]
for j in range(len(list1)):
  if list1[j]>list1[0]:
    lar=list1[j]
print(lar)
scb=list1[0]
for i in range(len(list1)):
  if list1[i]>scb:
    if list1[i]<lar:
      scb=list1[i]
print(scb)
