class A :
    def m1(self):
        print('in m1')
    def m2(self):
        print('in m2')

class B(A):
    def m3(self):
        print('in m3')

obj = B()
obj.m3()
obj.m1()
obj.m2()