# lambda

# Lambda is a small anonymous(nameless) function defined in a single line.

# Lambda expressions (sometimes called lambda forms) are used to create
# anonymous functions. The expression "lambda parameters: expression"
# yields a function object.  The unnamed object behaves like a function
# object defined with:
# def <lambda>(parameters):
#        return expression


v = lambda a : a+1
print(type(v))
# <class 'function'>

print(v(5))
# 6

# Multiply 2 numbers using lambda function
m = lambda a,b:a*b
print(m(4,2))
# 8

# In a single line
print((lambda a,b:a*b)(6,4))
# 24

