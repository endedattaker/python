#concatenation
list=[1,2,3]
list1=[1,2,3]
print(list+list1)

#reverse
list=[1,2,3]
print(list[::-1])

#reverse
list=[1,2,3]
rev=[]
for i in list:
  rev=[i]+rev
print(rev)

list = [1, 2, 3, 4, 5]
#print("List before reverse : ",original_list)
revlist = []
for i in list:
  revlist = [i] + revlist
print("List after reverse : ", revlist)
