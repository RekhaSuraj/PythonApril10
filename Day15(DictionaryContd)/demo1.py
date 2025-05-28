# update() - appends one dictionary with another. (It adds 2 or more dictionaries)

d1 = {10:'red',11:'blue',12:'pink',13:'orange'}

d1.update({1:'brown',2:'white'})
print(d1)

# {10: 'red', 11: 'blue', 12: 'pink', 13: 'orange', 1: 'brown', 2: 'white'}

# or
d2 = {20:'black'}
d1.update(d2)
print(d1)
# {10: 'red', 11: 'blue', 12: 'pink', 13: 'orange', 1: 'brown', 2: 'white', 20: 'black'}