#vowel checking
a= "Helloworld"
b="aeiouAEIOU"
v=0
la=len(a)
lb=len(b)
for i in range(la):
  for j in range(lb):
    if a[i]==b[j]:
      v=v+1
      break
    
print(v)
