# Bitwise operators - Works mostly on binaries (0, 1)
# There are 6 bitwise operators
# Bitwise and (&)- ampersand
# Bitwise or (|)- pipe
# Bitwise not (~)- tilde
# Bitwise XOR (^) - cap
# Bitwise Shiftleft (<<)
# Bitwise Shiftright (>>)

# Bitwise and (&) - Performs and operation on binaries of the numbers

print(9 & 5)
# 1

# 5 --> 0  1  0  1
# 3 --> 0  0  1  1
# & --------------
#       0  0  0  1 - > 1


print(5 & 3)
# 1

print(8 & 10)
# 8

# 8 --> 1  0  0  0
# 10 -->1  0  1  0
# & --------------
		# 1  0  0  0 - > 8