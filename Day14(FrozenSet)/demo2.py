fz = frozenset([11,'hi','hello',22,33,44,55])
# copy() - Return a shallow copy of a set.
fz1 = fz.copy()
print(fz1)
# frozenset({33, 11, 44, 'hello', 55, 22, 'hi'})

fz2 = frozenset({10,20,30,40,50})
fz3 = frozenset({10,20,30})

# difference()
# Return the difference of two or more sets as a new set.
# (i. e. all elements that are in this set but not the others.)

print(fz2.difference(fz3))
# frozenset({40, 50})

# union() - Return the union of sets as a new set.
# (i. e. all elements that are in either set.)
print(fz2.union(fz3))
# frozenset({50, 20, 40, 10, 30})

# issuperset()- Report whether this set contains another set
print(fz2.issuperset(fz3))
# True

# issubset() - Report whether another set contains this set
print(fz3.issubset(fz2))
# True

# intersection() - Return the intersection of two sets as a new set.
# (i. e. all elements that are in both sets.)
print(fz2.intersection(fz3))
# frozenset({10, 20, 30})

# isdisjoint() - Return True if two sets have a null intersection
print(fz2.isdisjoint(fz3))
# False

# symmetric_difference() - Return the symmetric difference of two sets as a new set.
# (i. e. all elements that are in exactly one of the sets.)
print(fz2.symmetric_difference(fz3))
# frozenset({40, 50})