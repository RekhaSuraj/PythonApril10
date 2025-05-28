# Tuple allows indexing
# Tuple is a ordered collection datatype(have a unique index values)

t = (11,33,44,22,55,'Welcome',77,66,'hi')

print(t[0])
# 11

# print 'Welcome'
print(t[5])
# Welcome

# index() - Return first index of value
print(t.index(77))
# 6

# We get error if we search for index number not in the tuple or not after the start index specified
print(t.index(77,7))
# ValueError: tuple.index(x): x not in tuple