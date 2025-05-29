# Update instance variables using instance methods
class Employee:
    def __init__(self,e_Name, e_IdNum, e_Role, e_Technology):
        self.name = e_Name
        self.IdNum = e_IdNum
        self.role = e_Role
        self.technology = e_Technology

    def display(self):
        print(f'Name:{self.name}')
        print(f'IDNum: {self.IdNum}')
        print(f'Role: {self.role}')
        print(f'Technology: {self.technology}')

    def update_fun(self):
        self.IdNum = 5678

    def delete_fun(self):
        del self.IdNum

    def upper_case(self):
        self.name = self.name.upper()


obj_emp1 = Employee('Lakshmi',1234,'DEVELOPER','PYTHON')
obj_emp1.display()

# Name:Lakshmi
# IDNum: 1234
# Role: DEVELOPER
# Technology: PYTHON

print()

obj_emp1.update_fun()
obj_emp1.display()

# Name:Lakshmi
# IDNum: 5678
# Role: DEVELOPER
# Technology: PYTHON

print()
# obj_emp1.delete_fun()
# obj_emp1.display()

# AttributeError: 'Employee' object has no attribute 'IdNum'

obj_emp1.upper_case()
obj_emp1.display()

# Name:LAKSHMI
# IDNum: 5678
# Role: DEVELOPER
# Technology: PYTHON