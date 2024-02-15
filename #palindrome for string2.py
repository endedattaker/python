#palindrome for string
a="alan"
c=a
b=""
for i in a:
  b=i+b
print(b)
if c==b:
  print("palindrome")
else:
  print("not palindrome")
