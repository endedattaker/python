class Student:
    def display(self):
        print("hi")
class Student2:
    def display2(self):
        print("world ")
class Child(Student,Student2):
    def exam(self):
        print("hello")
obj=Child()
obj.display()
obj.display2()
obj.exam()