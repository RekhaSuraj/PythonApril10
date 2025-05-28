# For integer operations, we have to convert user input to int
# Addition operation
n1 = int(input('Enter first number'))
n2 = int(input('Enter second number'))

print(type(n1))
print(type(n2))

res_add = n1+n2
print("addition:",res_add)

# Enter first number5
# Enter second number7
# <class 'int'>
# <class 'int'>
# 12

# Subtraction
res_sub = n1 - n2
print("subtraction:", res_sub)

# <class 'int'>
# <class 'int'>
# addition: 50
# subtraction: 10

# hw - Mutiplication, Division, Floor Division, Expo