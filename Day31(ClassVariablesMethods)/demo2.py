# Update class variable in an instance method

class Employee:

    company = 'TCS'
    def __init__(self,e_name, e_Idnum):
        self.name = e_name
        self.eId = e_Idnum


    def show(self):
        print(f'Name:',self.name)
        print(f'Id:',self.eId)
        print(f'Company Name:',self.company)

    # Update class variable inside an instance method
    def update_class_var(self,new_company):
        self.company = new_company
        # Employee.company = new_company

    def delete_class_var(self):
        # del self.company
        del Employee.company


obj_Emp = Employee('ABC',1234)
obj_Emp.show()
print()
obj_Emp.update_class_var('Wipro')
obj_Emp.show()
#
# Name: ABC
# Id: 1234
# Company Name: TCS
#
# Name: ABC
# Id: 1234
# Company Name: Wipro
print()
obj_Emp.delete_class_var()
obj_Emp.show()

# AttributeError: 'Employee' object has no attribute 'company'