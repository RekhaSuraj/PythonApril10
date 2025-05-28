# Default Arguments
# In a function, arguments can have default values.
# We assign default values to the argument using the ‘=’ (assignment) operator at the time of function definition(declaration).
# You can define a function with any number of default arguments.


def profile(name='Test',age=20,salary=30000,company='GRK'):
    print(f'Name:{name}')
    print(f'Age:{age}')
    print(f'Salary:{salary}')
    print(f'Company:{company}')


profile()

# Name:Test
# Age:20
# Salary:30000
# Company:GRK

# If no parameters are passed, it will take default arguments,
# We can update the parameters by overriding them and passing different parameters
# Here name is overridden
print()
profile('Lakshmi')
# Name:Lakshmi
# Age:20
# Salary:30000
# Company:GRK

# Here name and age are overridden
print()
profile('Lakshmi',16)

# Name:Lakshmi
# Age:16
# Salary:30000
# Company:GRK

# All parameters are overridden
print()
profile('Lakshmi',age=25,salary=60000,company='NTTDATA')

# Name:Lakshmi
# Age:25
# Salary:60000
# Company:NTTDATA
