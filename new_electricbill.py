units=int(input("enter units used in a month"))
if units<=100:
  print(units*0.5)
elif (units>100) and (units<=150):
 print((100*0.5)+(units-100)*0.75)
elif (units>150) and (units<=200):
  print((100*0.5)+(50*0.75)+(units-150)*1)
else:
    print((100*0.5)+(50*0.75)+(50*1)+(units-200)*2)
