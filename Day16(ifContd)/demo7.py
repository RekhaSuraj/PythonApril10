# Typecasting or type conversion

# convert a list to a tuple
# list1 = [10,20,30,40,50,60]
# print('Before conversion:',type(list1))
#
# t1 = tuple(list1)
# print(t1)
# print('After conversion:',type(t1))

# Before conversion: <class 'list'>
# (10, 20, 30, 40, 50, 60)
# After conversion: <class 'tuple'>

# Convert from tuple to list
# t2 = (11,22,33,44,55)
# print('Before conversion:',type(t2))
# l2 = list(t2)
# print(l2)
# print('After conversion:',type(l2))

# Before conversion: <class 'tuple'>
# [11, 22, 33, 44, 55]
# After conversion: <class 'list'>

# convert from set to list
# s1 = {5,10,15,20,25,30}
# print('Before conversion:',type(s1))
#
# l3 = list(s1)
# print(l3)
# print('After conversion:',type(l3))

# Before conversion: <class 'set'>
# [20, 5, 25, 10, 30, 15]
# After conversion: <class 'list'>

# Convert from list to set: Removes duplicates
l2 = [30,20,77,89,10,34,20,77]
print('Before conversion:',type(l2))

s2 = set(l2)
print(s2)
print('After conversion:',type(s2))

# Before conversion: <class 'list'>
# {34, 10, 77, 20, 89, 30}
# After conversion: <class 'set'>