class Overriding:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'Hello {self.a},{self.b}'

    def __add__(self, other):
        return f'{self.a + other.a},{self.b + other.b}'


# This tells Python how to behave when you write obj1 + obj2.
# Instead of the default behavior (which would raise an error), it adds the a and b values from both objects and returns a formatted string.

obj_Overriding = Overriding(5,10)
print(obj_Overriding)
# Hello 5,10


obj_Overriding2 = Overriding(20,30)
print(obj_Overriding2)
# Hello 20,30

res = obj_Overriding + obj_Overriding2
print(res)


# Calls __add__:
# self.a = 5, self.b = 10
# other.a = 20, other.b = 30
# Result: 5+20 = 25, 10+30 = 40
# Returns: 25,40