class A:
    def m3(self):
        print("in m3 from A")

class B :
    def m3(self):
        print("in m3 from B")

class C(B,A):
    def m3(self):
        super().m3()
        print("in m3 from c")

obj=c()
obj.m3()