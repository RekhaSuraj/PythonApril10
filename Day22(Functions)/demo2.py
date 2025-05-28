print('Before function')

def hello_function():
    print('Welcome to GRK')


print('Outside the function')
hello_function()
print('After function execution')

print(type(hello_function))
# <class 'function'>

# Before function
# Outside the function
# Welcome to GRK
# After function execution