Course = 100
class A:
    course = "python"
    def m1(self):
        print("In m1 from A")
        print(A.course)
        print(Course)
obj = A()
obj.m1()