s = {5,10,15,20,25,30}
# copy() - Returns a shallow copy of a set
s1 = s.copy()
print(s1)
# {20, 5, 25, 10, 30, 15}

# update() - Update a set with the union of itself and others
s2 = {'hi','Welcome','hello','GRK'}
s.update(s2)
# first set gets extended or updated
print(s)
# {5, 10, 'GRK', 'hello', 15, 20, 'hi', 'Welcome', 25, 30}
print(s2)
# {'GRK', 'hi', 'hello', 'Welcome'}

# clear() - clears all the elements in the set and returns an empty set
s2.clear()
print(s2)
# set()