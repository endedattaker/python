#list integer from user input odd and even lists
a=int(input("limit:"))
b=[]
c=[]
for i in range(a):
  ele=int(input())
  if ele%2==0:
    b.append(ele)
  else:
    c.append(ele)
print(b)
print(c)    
