l1 = [10,20,30]
# dict.fromkeys() - Create a new dictionary with keys from iterable and values set to value

d1 = dict.fromkeys(l1)
print(d1)
# {10: None, 20: None, 30: None}

d2 = dict.fromkeys(l1,'numbers')
print(d2)
# {10: 'numbers', 20: 'numbers', 30: 'numbers'}

t1 = (11,22,33,44)
d3 = dict.fromkeys(t1,'test')
print(d3)
# {11: 'test', 22: 'test', 33: 'test', 44: 'test'}