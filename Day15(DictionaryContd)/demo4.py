d1 = {'name':'Lakshmi','age':25,'location':'kadapa'}
# print(help(dict.setdefault))
# setdefault(self, key, default=None, /)
#     Insert key with a value of default if key is not in the dictionary.
#
#     Return the value for key if key is in the dictionary, else default.

print(d1.setdefault('salary',50000))
# 50000
print(d1)
# {'name': 'Lakshmi', 'age': 25, 'location': 'kadapa', 'salary': 50000}

# print(d1.setdefault('location','kadapa'))
# kadapa
# print(d1)