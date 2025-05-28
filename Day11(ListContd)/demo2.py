list1 = [33,22,10,11,22,55,88,66]
# count() - Return number of occurrences of value
print(list1.count(22))
# 2

print(list1.count(88))
# 1

print(list1.count(44))
# 0

# copy() - Return a shallow copy of the list
list2 = list1.copy()
print(list2)

# [33, 22, 10, 11, 22, 55, 88, 66]