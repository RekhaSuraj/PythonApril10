# Let’s see how to create a factory method using the class method.
# A factory method in Python is a design pattern used to create objects. Instead of calling the constructor (__init__) directly to create an object,
# you use a method (often a @classmethod) that returns an instance of the class — sometimes with custom initialization logic.
#
# Why Use a Factory Method?
# To encapsulate object creation logic
# To return different subclasses based on input
# To reuse code for multiple ways of creating objects
# To give meaningful names to ways of creating an object
from datetime import date
class Student:
    def __init__(self,Name, Age):
        self.Name = Name
        self.Age = Age

    @classmethod
    def calculate_age(cls,birth_year, name):
        # print(date.today().year)
        age = date.today().year - birth_year
        return cls(name,age)

    def display_age(self):
        return f'{self.Name} age is {self.Age}'

# ob1 = Student('ABC',25)


var1 = Student.calculate_age(1998,'Seetha')
# print(var1)
# print(var1.Age)
# print(var1.Name)


print(var1.display_age())
# Seetha age is 27


