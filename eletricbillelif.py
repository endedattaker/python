units=int(input("enter units used in a month"))
if units <= 100:
      print(units * 10) 
elif units <= 200:
      print(((100 * 10) +(units - 100) * 15))
elif units <= 300:
     print(((100 * 10) +(100 * 15) +(units - 200) * 20))
else :
      print( ((100 * 10) +(100 * 15) +(100 * 20) +(units - 300) * 25))
