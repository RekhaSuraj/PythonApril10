# set -
# Set is an unordered collection of unique elements, set does not support index
# set is declared inside flower braces
# insertion order is not preserved, does not allow duplicates
# Mutable: You can modify a set by adding or removing elements (add(), remove(), discard(), pop(), clear()).
# Elements Must Be Immutable: You cannot have lists or other sets as elements in a set because they are
# not hashable.
# Set does not allow duplicates

# how do we declare a set
s1 = {10,20,30,40,'hi','welcome'}
print(type(s1))
# <class 'set'>

# empty set - using constructor
s = set()
print(type(s))
# <class 'set'>

# If we write empty flower brackets, it is considered as empty dictionary
s2 = {}
print(type(s2))
# <class 'dict'>

s3 = set({10,20,30,40,50})
print(type(s3))
# <class 'set'>
print(s3)
# {50, 20, 40, 10, 30}


