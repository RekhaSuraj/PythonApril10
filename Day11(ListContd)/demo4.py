# Slicing
# list[start:stop:step]

list1 = [10,30,40,50,5,'hello','hi','world']

print(list1[6::])
# ['hi', 'world']

# 5,'hello','hi'
print(list1[4:7])
# [5, 'hello', 'hi']

# -ve slicing
# 40,50,5
print(list1[-6:-3])
# [40, 50, 5]

# print in reverse order
print(list1[::-1])
# ['world', 'hi', 'hello', 5, 50, 40, 30, 10]