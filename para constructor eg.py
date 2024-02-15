class Stud:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def disp(self):
        print("name:%s \n age:%d" %(self.name,self.age))
s1=Stud("abhi",23)
s1.disp()