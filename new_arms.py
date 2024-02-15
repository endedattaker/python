num=int(input("Enter any Number : "))
arms=0
temp=num
l=len(str(num))
while (num>0):
    rem=num%10
    arms=arms+(rem**l)
    num=num//10
if temp==arms:   
  print("armsrtong number : ")
else:
    print("not armsrtong number : ")
