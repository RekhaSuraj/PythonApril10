# INDEXING in Strings
# It indicates the index or position of every character in the string
# Positive indexing starts from 0 and goes till n-1(full length is n). It moves from left to right

str1 = "Knowledge is Power"

print('index value at 0:',str1[0])
print('index value at 1:',str1[1])
print('index value at 2:',str1[2])
print('index value at 3:',str1[3])
print('index value at 4:',str1[4])
print('index value at 5:',str1[5])
print('index value at 6:',str1[6])
print('index value at 7:',str1[7])
print('index value at 8:',str1[8])
print('index value at 9:',str1[9])
print('index value at 10:',str1[10])
print('index value at 11:',str1[11])
print('index value at 12:',str1[12])
print('index value at 13:',str1[13])
print('index value at 14:',str1[14])
print('index value at 15:',str1[15])
print('index value at 16:',str1[16])
print('index value at 17:',str1[17])

# index value at 0: K
# index value at 1: n
# index value at 2: o
# index value at 3: w
# index value at 4: l
# index value at 5: e
# index value at 6: d
# index value at 7: g
# index value at 8: e
# index value at 9:
# index value at 10: i
# index value at 11: s
# index value at 12:
# index value at 13: P
# index value at 14: o
# index value at 15: w
# index value at 16: e
# index value at 17: r

# If we try to access index which is not present in the string
# print('index value at 18:',str1[18])
# IndexError: string index out of range

# print 'w' from the above string
print(str1[15])
# w