# Bitwise shiftleft (<<)
# Shifts the position of the binary to left (according to the number of positions given)
# This adds the bits 
x = 5
print(x<<1)
# 10

print(x<<2)
# 20

# 4 << 1 
#    	0 1 0 0 (4 in binary) 
# << 1  
# ---------------
#       1 0 0 0 (8 in binary)


# Bitwise shiftright(>>)
# Shifts the position of the binary to right (according to the number of positions given)
# This looses the bits 
a = 5
print(a >> 1)
# 2

# 5 >> 1 
#    	0 1 0 1 (5 in binary) 
# >> 1  
# ---------------
#       0 0 1 0 (2 in binary)


print(7 >> 2)
# 1