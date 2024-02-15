class A:
    def display(self):
        print("hi")
class B(A):
    def display2(self):
        print("world ")
class C(B):
    def exam(self):
        print("hello")
obj=C()
obj.display()
obj.display2()
obj.exam()