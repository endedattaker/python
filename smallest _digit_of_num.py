num=int(input("Enter any Number : "))
max=9
while num>0:
    digit=num%10
    if digit<max:
        max=digit
    num=num//10
print("smallest Digit is : ",max)
