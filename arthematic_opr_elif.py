print("1.sum")
print("2.sub")
print("3.mul")
print("4.ediv")

r=int(input("enter choice:"))



if r==1:
    a=int(input("enter number1:"))
    b=int(input("enter number2:"))
    sum=a+b
    print("sum of "+str(a)+"+"+str(b)+"="+str(sum))
    #print("sum=",a+b)
elif r==2:
    a=int(input("enter number1:"))
    b=int(input("enter number2:"))
    print("sub=",a-b)
elif r==3:
    a=int(input("enter number1:"))
    b=int(input("enter number2:"))
    print("mul=",a*b)
elif r==4:
    a=int(input("enter number1:"))
    b=int(input("enter number2:"))
    print("div=",a/b)
   
else:
    print("invalid")
