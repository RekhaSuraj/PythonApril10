# Simple calculator program

num1 = int(input('Enter first number'))
num2 = int(input('Enter second number'))

operation = input('Enter the operation you want to perform')

if operation == '+':
    print(f'Addition of {num1} and {num2} is {num1+num2}')

if operation == '-':
    print(f'Subtraction of {num1} and {num2} is {num1-num2} ')

if operation == '*':
    print(f'Multiplication of {num1} and {num2} is {num1*num2}')

#
# Enter first number10
# Enter second number5
# Enter the operation you want to perform+
# Addition of 10and 5 is 15


# Enter first number20
# Enter second number10
# Enter the operation you want to perform-
# Subtraction of 20 and 10 is 10

# Enter first number20
# Enter second number5
# Enter the operation you want to perform*
# Multiplication of 20 and 5 is 100

# hw - Division, Floordivsion, exponentiation, modulus