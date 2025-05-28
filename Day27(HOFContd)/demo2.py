# reduce

from functools import reduce

# syntax :reduce(function, iterable[, initial])
# reduce() works by calling the function we passed for the first two items in the sequence.
# The result returned by the function is used in another call to function alongside with the
# next (third in this case), element.

# function: A function that takes two arguments.
# iterable: A sequence (like a list).
# initializer (optional): A value that is used as the initial value.

list1 = [10,20,30,40,50,60,70,80,90]

def sum_add(n1,n2):
    return n1 + n2

print(reduce(sum_add,list1))
# 450


# How it works:
# reduce() applies the lambda function cumulatively to the items of the list.

# First it does: 10 + 20 → 30

# Then: 30 + 30 → 60

# Then: 60 + 40 → 100

# Then: 100 + 50 → 150

# Then: 150 + 60 → 210
# It will continue like this
print()
def prod_fun(a,b):
    return a * b

print(reduce(prod_fun,list1))
# 362880000000000

print()
# using range
print(reduce(sum_add,range(21)))
# 210

# using lambda
print(reduce(lambda a,b:a+b,range(21)))
# 210

print(reduce(lambda x,y:x+y, list1))
# 450