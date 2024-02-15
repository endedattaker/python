class Student:
    def display(self):
        print("hi")
class Child(Student):
    def exam(self):
        print("hello")
obj=Child()
obj.display()
obj.exam()