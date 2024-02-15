num=int(input("Enter any Number : "))
max=0
while num>0:
    digit=num%10
    if max<digit:
        max=digit
    num=num//10
print("Largest Digit is : ",max)
