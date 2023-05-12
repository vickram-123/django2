class Employee:
    Company_name = "Infosys"

    def __init__(self,id,name,sal):
        self.id = id
        self.name = name
        self.sal = sal

    def show (self):
        print("Company Name:",Employee.Company_name)
        print("Id",self.id)
        print("Name",self.name)
        print("Sal",self.sal)
        bonous=self.bonous_cal(self.sal)
        print("**"*25)
        print("Total sal before Bonous::",self.sal)
        print("Total sal After Bonous::",self.sal+bonous)
        print("*"*25)

    def bonous_cal(self,sal):
        b= (self.sal*0.15)
        return b

obj = Employee(101,"Vicky",75000)
obj.show()


