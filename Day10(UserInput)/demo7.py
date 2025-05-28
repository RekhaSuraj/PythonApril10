l1 = ['Lakshmi','GRK','Hello','Hi']
# append() - Append object to the end of the list.
l1.append('Welcome')
# append() - does not return anything - None
# var = l1.append('Welcome')
# print(var)
# None

print(l1)
# ['Lakshmi', 'GRK', 'Hello', 'Hi', 'Welcome']

# pop() - Remove and return item at index (default last).
v1 = l1.pop(2)
print(v1)
# Hello

print(l1)
# ['Lakshmi', 'GRK', 'Hi', 'Welcome']

# remove() - Remove first occurrence of value.
# Raises ValueError if the value is not present.
l1.remove('Hi')
print(l1)
# ['Lakshmi', 'GRK', 'Welcome']

# l1.remove('Hi')
# ValueError: list.remove(x): x not in list