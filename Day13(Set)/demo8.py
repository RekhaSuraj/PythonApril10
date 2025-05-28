s = {1,2,3,4,5,6,7}
s1 = {1,2,3,8}

# union - Return the union of sets as a new set.
# (i. e. all elements that are in either set.)
new_set = s.union(s1)
print(new_set)
# {1, 2, 3, 4, 5, 6, 7, 8}

# IMP: Difference between remove() and discard()
# Remove an element from a set if it is a member.
# Unlike set. remove(), the discard() method does not raise an exception when an element is missing from the set.
s.discard(7)
print(s)
# {1, 2, 3, 4, 5, 6}

s.discard(10)
print(s)
# {1, 2, 3, 4, 5, 6}

# hw
# s.symmetric_difference(s1)
# s.isdisjoint(s1)
# s.symmetric_difference_update(s1)