# Membership Operators - There are 2 membership operators (in, not in).
# It acts on only iterables - list, set, tuple

list1 = [10,20,30,40,'Lakshmi','GRK','Hello']


# in operator - returns True if an item is present in the iterable
print(20 in list1)
# True

print('Lakshmi' in list1)
# True

print('abc' in list1)
# False

print('*********')
# not in operator - Returns True if an item is not present in the iterable
print('abc' not in list1)
# True

print(30 not in list1)
# False