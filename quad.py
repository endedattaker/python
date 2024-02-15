a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
r=(b*b) - (4*a*c)
if r>0:
    x1=-b+(r**(0.5))/2*a
    x2=-b-(r**(0.5))/2*a
    print("roots are real and distinct")
    print(x1,x2)

    #print(r)
elif r==0:
    x1=-b+(r**(0.5))/2*a
    x2=-b-(r**(0.5))/2*a

    print("roots are real and equal")
    print(x1,x2)
else:
    print("roots are complex or imaginary")
    #print(r)
   


