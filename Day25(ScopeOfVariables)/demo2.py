# Global Variable

# A global variable is variable , which is defined outside the function,
# we access anywhere inside and outside of the function.

name1 = 'Lakshmi' # Global variable
print(f'Global variable outside the function')
def greetings():
    age = 20
    print(f'GLobal variable inside the function:{name1}')
    print(f'Local variable:{age}')


greetings()
print(name1)
# Global variable outside the function
# GLobal variable inside the function:Lakshmi
# Local variable:20
# Lakshmi