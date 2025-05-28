# Nested List - lists inside another list
list1 = [10,20,30,['hi','hello',40],[50,60],70,80]

print('value at index 0:',list1[0])
print('value at index 1:',list1[1])
print('value at index 2:',list1[2])
print('value at index 3:',list1[3])
print('value at index 4:',list1[4])
print('value at index 5:',list1[5])
print('value at index 6:',list1[6])

# value at index 0: 10
# value at index 1: 20
# value at index 2: 30
# value at index 3: ['hi', 'hello', 40]
# value at index 4: [50, 60]
# value at index 5: 70
# value at index 6: 80

# print hello from above list
print(list1[3][1])
# hello

print(list1[4][0])
# 50

# -ve indexing
print('value at index -1:',list1[-1])
print('value at index -2:',list1[-2])
print('value at index -3:',list1[-3])
print('value at index -4:',list1[-4])
print('value at index -5:',list1[-5])
print('value at index -6:',list1[-6])
print('value at index -7:',list1[-7])

# value at index -1: 80
# value at index -2: 70
# value at index -3: [50, 60]
# value at index -4: ['hi', 'hello', 40]
# value at index -5: 30
# value at index -6: 20
# value at index -7: 10


# 50 using -ve indexing
print(list1[-3][-2])
# 50

# print hi using -ve indexing
print(list1[-4][-3])
# hi