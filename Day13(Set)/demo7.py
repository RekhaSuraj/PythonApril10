s = {5,10,15,20,25,30}
s1 = {5,10,15}

# Return the intersection of two sets as a new set.
# (i. e. all elements that are in both sets.)
print(s.intersection(s1))
# {10, 5, 15}

# intersection_update() - Update a set with the intersection of itself and another
s.intersection_update(s1)
print(s)
# {10, 5, 15}
print(s1)
# {10, 5, 15}


