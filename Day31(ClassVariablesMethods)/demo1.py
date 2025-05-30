# Class Variables:
# Class Variables: A class variable is a variable that is declared inside of class,
# but outside of any instance method or __init__() method.

class Student:

    # class variable
    school_name = 'KGBVSchool'

    def __init__(self,s_name, s_age,s_class,s_gender):
        self.name = s_name
        self.age = s_age
        self.stu_class = s_class
        self.gender = s_gender
        self.school_name = 'DPS'


    def show(self):
        print(f'Name:',self.name)
        print(f'Age:',self.age)
        print(f'Class:',self.stu_class)
        print(f'Gender:',self.gender)
        # if we have an instance variable with the same name, it will override class var
        print(f'SchoolName:',self.school_name) # DPS
        # classname.classvariable will fetch only class var
        print(Student.school_name) # KGBVSchool



# obj_Student = Student('Lakshmi',20,10,'F')
# print(obj_Student.school_name)
# obj_Student.show()

ob1 = Student('Rama',200,5,'M')
ob2 = Student('Seetha',250,12,'F')
ob3 = Student('Krishna',30,9,'M')
ob4 = Student('GRK',5,10,'M')

all_obs = [ob1,ob2,ob3,ob4]

for ob in all_obs:
    ob.show()
    print()



