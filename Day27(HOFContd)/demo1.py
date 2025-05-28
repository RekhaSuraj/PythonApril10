# Fetch the sum of all the squares of odd numbers from 1 to 20
# Fetch odd numbers using filter from 1 to 20

print(list(filter(lambda a: a%2 != 0,range(21))))
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Square of all the above numbers
print(list(map(lambda x: x**2, list(filter(lambda a: a%2 != 0,range(21))))))
# [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]

# sum of all the above squares
print(sum(list(map(lambda x: x**2, list(filter(lambda a: a%2 != 0,range(21)))))))
# 1330

# max of all numbers in the list
print(max(list(map(lambda x: x**2, list(filter(lambda a: a%2 != 0,range(21)))))))
# 361