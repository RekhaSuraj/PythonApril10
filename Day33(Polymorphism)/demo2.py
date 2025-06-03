# Manager: Name, Age, Gender, No of Teams, Location, Salary

class Manager:

    def __init__(self,m_name, m_age, m_gender, m_Teams, m_location, m_salary):
        self.m_Name = m_name
        self.m_Age = m_age
        self.m_Gender = m_gender
        self.m_Teams = m_Teams
        self.m_Location = m_location
        self.m_Salary = m_salary


    def display(self):
        print(f'Name:{self.m_Name}\n Age:{self.m_Age}\n Gender:{self.m_Gender}\n Teams:{self.m_Teams}\n Location:{self.m_Location}\n Salary:{self.m_Salary}')



obj_Mgr = Manager('Lakshmi',25,'F',5,'Bangalore',200000)

obj_Mgr.display()

# Name:Lakshmi
#  Age:25
#  Gender:F
#  Teams:5
#  Location:Bangalore
#  Salary:200000


