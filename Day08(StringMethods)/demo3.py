s3 = "Python Developer"

# count() - Return the number of non-overlapping occurrences of substring sub in string S[start:end].
# Optional arguments start and end are interpreted as in slice notation
# count() - Returns number of occurrences of a substring in a given string
print(s3.count("o"))
# 2

s = s3.lower()
print(s.count("p"))
# 2

print(s3.count("y"))
# 1

print(s3.count("x"))
# 0

# Giving start index and search for a substring, "o" has occurred only one time after 5th index here
print(s3.count("o", 5))
# 1