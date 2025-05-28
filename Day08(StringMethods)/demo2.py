# print(help(str))
str2 = "today is a good Day"

# capitalize() - Return a capitalized version of the string.
# More specifically, make the first character have upper case and the rest lower case.
print(str2.capitalize())
# Today is a good day

# index() - Returns the index number of the given letter.
# Throws error if substring is not found
print(str2.index("g"))
# 11

# Returns the index number - starts to search from a specified start index(Here we have given 2)
print(str2.index("o",2))
# 12

# Starts to search from a specified index and stops searching at specified given index(Here start at 13 and search till 15)
print(str2.index('o',13,15))
# 13

print(str2.index('z'))
# ValueError: substring not found