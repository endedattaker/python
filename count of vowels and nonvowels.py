#count of vowels and nonvowels
String = str(input('Enter the string :'))
count=0
notv=0
String = String.lower()
for i in String:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
      count+=1
    else:
      notv+=1


print('Total vowels are :',count)
print('Total vowels are :',notv)
