num=int(input("Enter any Number : "))
lar=0
for digit in str(num):
  digit=int(digit)
  if digit>lar:
    lar=digit
print("largest digit is=",lar)
