n=123
temp=n
rev=""
for i in str(n):
  rev=i+rev
print(rev)
if temp==int(rev):
  print("palindrome")
else:
  print("not palindrome")
