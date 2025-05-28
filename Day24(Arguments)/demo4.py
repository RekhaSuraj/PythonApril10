#Variable-Length Arguments in Python (*args and **kwargs)
# In Python, functions can accept a variable number of arguments using:
#
# *args → Variable-length positional arguments (Tuple)
#
# **kwargs → Variable-length keyword arguments (Dictionary)
#
# 1. Using *args (Multiple Positional Arguments)
# ✅ Allows a function to accept any number of positional arguments.
# ✅ Collects them into a tuple.


def profile(*args):
    for i in args:
        print(i)


profile('hello','hi','welcome',10,20,30)
# hello
# hi
# welcome
# 10
# 20
# 30

print()
def sum_numbers(*nums):
    return sum(nums) #nums is a tuple of values


print(sum_numbers(10,20,30,1,2,3))
print(sum_numbers(1,5,10))
# 66
# 16

# Return the sum of a 'start' value (default: 0) plus an iterable of numbers
print(sum_numbers())
# 0

print()
def multiply_numbers(*prod):
    res = 1
    for i in prod:
        res = res * i

    return res


mul = multiply_numbers(1,3,10,20)
print(mul)
# 600

print(multiply_numbers())
# 1