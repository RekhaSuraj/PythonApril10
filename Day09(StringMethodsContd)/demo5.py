s1 = "Hello World"
# split() - Return a list of the substrings in the string, using sep as the separator string
# If we have not specified any separator, it will take ""(whitespace)as separator by default
print(s1.split())

# separator - sep
# The separator used to split the string.
# When set to None (the default value), will split on any whitespace character (including
# and spaces) and will discard
#   empty strings from the result.

# Here separator is "-"
s2 = "Hello-Wor-ld"
print(s2.split("-"))
# ['Hello', 'Wor', 'ld']

s3 = "Welcome:To:Python:"
print(s3.split(":"))
# ['Welcome', 'To', 'Python', '']