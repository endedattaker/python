class A:
    def display(self):
        print("hi")
class B(A):
    def display2(self):
        print("world ")
class C(A):
    def exam(self):
        print("hello")
obj2=C()
obj=B()
obj.display()
obj.display2()
obj2.exam()