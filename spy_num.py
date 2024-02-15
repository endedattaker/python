num=int(input("Enter your number "))
sum=0
product=1
num1 = num
 
while(num>0):
    d=num%10
    sum=sum+d
    product=product*d
    num=num//10
 
if(sum==product):
    print(" a Spy number!")
else:
    print(" not a Spy number!")
