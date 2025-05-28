# Slicing - Fetching a part of the string
# syntax for writing a slicing expression: string[start:stop:step]

# start - Defines the start index from where we want to fetch the string/substring, default is 0
# stop - Defines the stop index till where we want to fetch the string/substring, it will stop one index before
# default is n-1
# step - jumps, steps for fetch, default value is 1

# Positive slicing

str1 = "Happiness is Everything"
print(len(str1))
# 23

# Fetch "Happi" from the above string
# Start value : 0
# Stop value : 5
# Step value : 1
print(str1[0:5:1])
# Happi

# without giving start value, because default is 0
print(str1[:5:1])
# Happi

# Without giving step and start, because default value of start is 0 and step is 1
print(str1[:5])
# Happi

# Fetch "Every" from the above string
# Giving start index from 13, stop index 18(it will stop at 17)
print(str1[13:18])
# Every

# is
print(str1[9:13])
# is

# giving step value - 2 - jumps upto 2nd index
print(str1[::2])
# "Happiness is Everything"
#  Hpiesi vrtig

# Happiness is Everything
# Without start, stop, step, string will be printed as it is
print(str1[::])