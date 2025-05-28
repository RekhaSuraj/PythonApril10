s = {11,22,44,33,55,88,99}
s1 = {11,22,44,10}
# difference() - Return the difference of two or more sets as a new set.
# (i. e. all elements that are in this set but not the others.)

print(s.difference(s1))
# {88, 33, 99, 55}

# difference_update - Remove all elements of another set from this set
s.difference_update(s1)
print(s)
# {33, 99, 55, 88}
print(s1)
# {10, 11, 44, 22}


