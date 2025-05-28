d1 = {1:'cat', 2: 'dog',3:'mouse',4:'elephant',5:'monkey'}
# get() - Return the value for key if key is in the dictionary, else default
print(d1.get(2))
# dog

# This can also fetched using index directly
print(d1[2])
# dog

# pop() - remove specified key and return the corresponding value.
# If the key is not found, return the default if given; otherwise, raise a KeyError.
print(d1.pop(3))
# mouse

print(d1)
# {1: 'cat', 2: 'dog', 4: 'elephant', 5: 'monkey'}

# If the key is not found, it raises a KeyError
# print(d1.pop(3))
# KeyError: 3

# print(help(dict.popitem))
# popitem(self, /)
#     Remove and return a (key, value) pair as a 2-tuple.
#
#     Pairs are returned in LIFO (last-in, first-out) order.
#     Raises KeyError if the dict is empty.


d1.popitem()
print(d1)
# {1: 'cat', 2: 'dog', 4: 'elephant'}

