# Set does not allow duplicates and does not retain insertion order
s = {11,22,33,44,55,66,66}
print(s)
# {33, 66, 22, 55, 11, 44}

# set methods
# add() - Add an element to a set.
s.add(10)
print(s)
# {33, 66, 22, 55, 10, 11, 44}

# Add an already existing element will not effect, set remains same. Does not throw error
s.add(44)
print(s)
# {33, 66, 22, 55, 10, 11, 44}
