# Overriding inbuilt methods
# The __str__() method returns a human-readable, or informal, string representation of an object.
# This method is called by the built-in print(), str(), and format() functions. If you don’t define a __str__()
# method for a class, then the built-in object implementation calls the __repr__() method instead.
# So __str__ is called in print(),str() and format(). So here let us override it and see from print() method


class Student:

    def __init__(self,x,y):
        self.x = x
        self.y = y


    def __str__(self):
        return f'Hello {self.x},{self.y}'


obj_Student = Student('Lakshmi','GRK')
print(obj_Student)

     


