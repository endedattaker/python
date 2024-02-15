#list
list=["abc",1, True ,9.6,9+8j]
print(list)
#list ordered,indexed
list=["abc",1, True ,9.6,9+8j]
print(list[2])
#list ordered,indexed
list=["abc",1, True ,9.6,9+8j]
print(list[-1])
#list ordered for loop
list=["abc",1, True ,9.6,9+8j]
for i in list:
  print(i)

#list adding values
list=["abc",1, True ,9.6,9+8j]
list[1]=2000
print(list)

#list append values
list=["abc",1, True ,9.6,9+8j]
list.append("python")
print(list)

#list insert values
list=["abc",1, True ,9.6,9+8j]
list.insert(1,"python")
print(list)

#list delete values
list=["abc",1, True ,9.6,9+8j]
del list[2]
print(list)

#list clear values
list=["abc",1, True ,9.6,9+8j]
list.clear()
print(list)

#list pop values
list=["abc",1, True ,9.6,9+8j]
list.pop()
print(list)

#list pop index values
list=["abc",1, True ,9.6,9+8j]
list.pop(3)
print(list)

#list from user input
a=int(input("limit:"))
b=[]
for i in range(a):
  ele=input()
  b.append(ele)
print(b)  

