# Dictionary

# Dictionary : Dictionary is used to store data in the form of key  : values
# Which is mutable ,ordered

# Creating a dictionary
# There are following three ways to create a dictionary.

# Using curly brackets: The dictionaries are created by enclosing the comma-separated Key: Value pairs
# inside the {} curly brackets.
# Keys must be unique.(No duplicates)
# Values can be of any data type and duplicates are allowed for values
# The colon ‘:‘ is used to separate the key and value in a pair.

dict1 = {}
print(type(dict1))
# <class 'dict'>

d1 = {1:'red',2:'blue',3:'pink'}
print(type(d1))
# <class 'dict'>
print(d1)
# {1: 'red', 2: 'blue', 3: 'pink'}