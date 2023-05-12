#super() method
class Employee():
    def __init__(self):
        pass
    def m1(self):
        print("Age")
        print("Name")
        print("City")

class Extended_emp(Employee):
    def m1(self):
        super().m1()
        print("Instagram id")

obj=Extended_emp()
obj.m1()