s1 = {20,30,10,40,50,'hi','hello'}
# pop() - removes an element from the set
s1.pop()
print(s1)
# {'hello', 20, 'hi', 40, 10, 30}

# remove() - Remove an element from a set; it must be a member

s1.remove(10)
print(s1)
# {20, 40, 'hello', 30, 'hi'}

# If the element is not a member, raise a KeyError
s1.remove(77)
print(s1)
# KeyError: 77