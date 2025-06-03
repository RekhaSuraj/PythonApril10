# common: Name, Age, Gender, Salary, Location
# Manager : No Of Teams
# Employee: TEchnology

class Profile:

    def __init__(self, p_Name, p_Age, p_Gender,p_Salary,p_Location):
        self.p_name = p_Name
        self.p_age = p_Age
        self.p_gender = p_Gender
        self.p_salary = p_Salary
        self.p_location = p_Location



class Manager(Profile):
    def __init__(self,Name, Age, Gender, Salary, Location, Teams):
        super().__init__(Name, Age, Gender, Salary,Location)
        self.m_Teams = Teams


    def display(self):
        print(
            f'Name:{self.p_name}\n Age:{self.p_age}\n Gender:{self.p_gender}\n Teams:{self.m_Teams}\n Location:{self.p_location}\n Salary:{self.p_salary}')


obj_Man = Manager('Rama',30,'M',20000,'BLR',10)
obj_Man.display()

# Name:Rama
#  Age:30
#  Gender:M
#  Teams:10
#  Location:BLR
#  Salary:20000

print()
class Employee(Profile):

    def __init__(self, Name, Age, Salary, Location, Gender, Technology):
        Profile.__init__(self, Name, Age, Salary, Location, Gender)
        self.e_Technology = Technology


    def display(self):
        print(f'Name:{self.p_name}\n Gender:{self.p_gender}\n Age:{self.p_age}\n Salary:{self.p_salary}\n Location:{self.p_location}\n Technology:{self.e_Technology}')

obj_Employee = Employee('ABC',25, 50000,'Mysore','F','Java')
obj_Employee.display()

# Name:ABC
#  Gender:50000
#  Age:25
#  Salary:Mysore
#  Location:F
#  Technology:Java