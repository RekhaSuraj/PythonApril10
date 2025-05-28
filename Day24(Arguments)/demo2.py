# Keyword Arguments
# Arguments are passed by parameter names, so order does not matter.

def profile(name,age,salary,company):
    print(f'Name:{name}')
    print(f'Age:{age}')
    print(f'Salary:{salary}')
    print(f'Company:{company}')


profile(name='Lakshmi',age='20',salary=60000,company='TCS')
# Name:Lakshmi
# Age:20
# Salary:60000
# Company:TCS

print('***************')
profile(age=20,company='Wipro',name='ABC',salary=50000)
# Name:ABC
# Age:20
# Salary:50000
# Company:Wipro

# Mixing positional and keyword arguments:
# Rule is first positional arguments should be declared first
# profile(age=20,50000,'Infosys',name='Rama')
# SyntaxError: positional argument follows keyword argument
print('***************')

profile('Seetha',200,company='CTS',salary=40000)
# Name:Seetha
# Age:200
# Salary:40000
# Company:CTS