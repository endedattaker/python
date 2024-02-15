class A:
    def display(self):
        print("hi")
class B(A):
    def display2(self):
        print("world ")
class C:
    def exam(self):
        print("hello")
class D(B,A):
    def exam2(self):
        print("hello hai")
obj=D()
obj2=C()
obj.display()
obj.display2()
obj.exam2()
obj2.exam()
