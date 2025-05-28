# Program to print numbers in reverse order

# Recursive function has 3 components:
# 1. Function Definition
# 2. Base case (Exit condition)
# 3. Recursive case


def rev_num(n): # Function Definition
    if n < 1:  # Base case (Exit condition)
        print('End')
    else:
        print(n)
        n = n-1
        rev_num(n)  # Recursive case

rev_num(5)

# 5
# 4
# 3
# 2
# 1
# End

