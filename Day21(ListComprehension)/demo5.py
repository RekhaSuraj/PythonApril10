# Convert to upper case
list1 = ['cow','cat','dog','hen','Goat']

upper_list = []
for i in list1:
    upper_list.append(i.upper())

print(upper_list)
# ['COW', 'CAT', 'DOG', 'HEN', 'GOAT']


# list comprehension
u_list = [i.upper() for i in list1]
print(u_list)
# ['COW', 'CAT', 'DOG', 'HEN', 'GOAT']
