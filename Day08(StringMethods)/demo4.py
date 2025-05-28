s = "Welcome to Python"
# find() - Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].
# Optional arguments start and end are interpreted as in slice notation.
# find() - Returns the index number of the specified substring
# If the substring is not found, it returns -1.
print(s.find("e"))
# 1

print(s.find("x"))
# -1

print(s.find("e",2))
# 6

