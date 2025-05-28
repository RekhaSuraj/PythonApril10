# Same variable declared in Global and local
# globals()- the dictionary containing the current scope's global variables.


name1 = 'Test'
def info():
    name1 = 'Lakshmi'
    print(f'Local variable:{name1}')
    print('Global variable:',globals()['name1'])

info()

print(name1)
# Local variable:Lakshmi
# Global variable: Test
# Test

