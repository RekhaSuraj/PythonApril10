# import module1

# We can call only specific methods using from module1 import
from module1 import addition_fun, subtraction_fun

# module1.addition_fun(5,10)
# 15

# addition_fun(10,20)
# 30

res = subtraction_fun(int(input('Enter first number')),int(input('Enter second number')))
print(res)

# Enter first number40
# Enter second number20
# 20

