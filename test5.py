#super methood
class A:
    def m1(self):
        print("in m1 from A")

class B(A):
    def m1(self):
        print("in m1 from Z")
class C(B):
    def m1(self):
        print("in m1 from B")
class D(C):
    def m1(self):
        super(B,self).m1()
        print("in m1 from A")

obj=D()
obj.m1()