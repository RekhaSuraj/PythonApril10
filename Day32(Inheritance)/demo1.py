# static methods:
# @staticmethod is a method inside a class that
# Does not need access to self(object)
# Does not need access to cls(class)

# It behaves like a normal function, but is placed inside a class for organization
# When to use staticmethod:
# WHen the method does not depend on class or object data

class Arithmetic_Tool:

    @staticmethod
    def add(x,y):
        return x+y

    @staticmethod
    def multiply(x,y):
        return x*y

var1 = Arithmetic_Tool.add(10,25)
print(var1)
# 35

res = Arithmetic_Tool.multiply(20,30)
print(res)
# 600

