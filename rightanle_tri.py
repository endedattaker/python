a=int(input("enter 1 side of triangle"))
b=int(input("enter 2 sides of triangle"))
c=int(input("enter 3 side of triangle"))
if (a*a+b*b==c*c) or (c*c+b*b==a*a) or (a*a+c*c==b*b) :
    print("The triangle is right-angled." )
else:
       print( "The triangle is not right-angled.")
