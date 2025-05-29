# Instance variables in Python are variables that belong to a specific instance(object) of a class
class Person:

    # Constructor
    def __init__(self,s_name,s_age,s_salary):
        self.c_name = s_name  #instance variable 1
        self.c_age = s_age #instance varaible 2
        self.c_salary = s_salary #instance variable 3

        print(self.c_name)
        print(self.c_age)
        print(self.c_salary)


obj_Person = Person('Lakshmi',20, 200000)
# Lakshmi
# 20
# 200000

print()
obj_Person2 = Person('GRK',5,300000)

# GRK
# 5
# 300000

