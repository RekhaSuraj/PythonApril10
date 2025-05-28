list1 = [11,22,66,33,'hi',44,55,66,6+8j]
# To access elements based on index
# syntax : listname[index_number]
print('value at index 0:',list1[0])
print('value at index 1:',list1[1])
print('value at index 2:',list1[2])
print('value at index 3:',list1[3])
print('value at index 4:',list1[4])
print('value at index 5:',list1[5])
print('value at index 6:',list1[6])
print('value at index 7:',list1[7])
print('value at index 8:',list1[8])

# value at index 0: 11
# value at index 1: 22
# value at index 2: 66
# value at index 3: 33
# value at index 4: hi
# value at index 5: 44
# value at index 6: 55
# value at index 7: 66
# value at index 8: (6+8j)

# index() - Return first index of value
print(list1.index('hi'))
# 3

print(list1.index(66,3))
# 7