# Higher Order Functions -

# map
# The map(), filter() and reduce() functions bring a bit of functional programming to Python.
#  All three of these are convenience functions that can be replaced with List Comprehensions or loops,
# but provide a more elegant and short-hand approach to some problems.

# The map() Function
# The syntax is:
# The map() function iterates through all items in the given iterable and executes the function
# we passed as an argument on each of them.


# syntax: map(function,iterable)
# Convert all the items in the list to upper using HOF(map)
def upper_fun(l):
    return l.upper()

list1 = ['Lakshmi','Welcome','Hello','GRK']

# using list
a = list(map(upper_fun,list1))
print(a)
# ['LAKSHMI', 'WELCOME', 'HELLO', 'GRK']

# using tuple
b = tuple(map(upper_fun,list1))
print(b)
# ('LAKSHMI', 'WELCOME', 'HELLO', 'GRK')

list2 = ['hello','world','bangalore','mysore']
# using lambda:
print(list(map(lambda a:a.upper(),list2)))

# ['HELLO', 'WORLD', 'BANGALORE', 'MYSORE']






