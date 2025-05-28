# Assignment operator
# There are following types of assignment operators
# = (Assign)
# += (Increment/Add and assign)
# -= (Decrement/Subtract and assign)
# *= (Multiply and assign)
# /= (Divide and assign)
# //= (Floor division and assign)
# %= (Modulus and assign)
# **= (Exponentiation and assign)

a = 10
# Here I am assigning 10 to variable a

x = 20
y = 30

z = x+y
print(z)
# 50

# Increment and assign
# I am reassigning value back to x
# x = x + 30
# print(x)

x += 30
# Is same as x = x+30
# print('using Increment and assign operator:',x)
# using Increment and assign operator: 50


# Decrement and assign
l = 10

l -= 5
# is same as l = l - 5
print('Decrement and assign:',l)
# Decrement and assign: 5

# Decrement using -ve numbers
m = -30
m -= 40

# m = m - 40
# m = -30 - 40
# m = -70

print(m)