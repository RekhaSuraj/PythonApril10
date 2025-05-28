# Negative slicing
# string[start:stop:step]

s1 = "Python is a high level programming language"
# fetch "language" from the above string using -ve slicing
print(s1[-8:])
# language

# Fetch "program" using -ve slicing
print(s1[-20:-13])
# program

# Always start index should be smaller than the stop index, otherwise it will give an empty string.Below is example
print(s1[-13:-20])

# Start from -20 and go till the end with 2 step jumps
print(s1[-20::2])
# pormiglnug

