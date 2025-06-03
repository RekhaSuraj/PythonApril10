# EMployee: Name, Gender, Age, Salary, Location, Technology
class Employee:
    def __init__(self, e_name,e_gender,e_age,e_salary,e_location,e_technology):
        self.e_Name = e_name
        self.e_Gender = e_gender
        self.e_Age = e_age
        self.e_Salary = e_salary
        self.e_Location = e_location
        self.e_Technology = e_technology

    def display(self):
        print(f'Name:{self.e_Name}\n Gender:{self.e_Gender}\n Age:{self.e_Age}\n Salary:{self.e_Salary}\n Location:{self.e_Location}\n Technology:{self.e_Technology}')


obj_Emp = Employee('Seetha','F',25,100000,'AP','Python')
obj_Emp.display()

# Name:Seetha
#  Gender:F
#  Age:25
#  Salary:100000
#  Location:AP
#  Technology:Python