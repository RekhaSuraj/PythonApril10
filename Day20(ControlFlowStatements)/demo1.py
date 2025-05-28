# control flow statements
# In Python, continue, break, and pass are control flow statements used in loops and conditional statements,
# but they behave differently:

# Statement	Function
# break		Exits the loop entirely
# continue	Skips the current iteration and continues to the next
# pass		Does nothing, acts as a placeholder


# 1. break
# Exits the loop completely.

# for i in range(5):
#     print(i)
#     if i == 2:
#         break
#
# print('outside loop')

# 0
# 1
# 2
# outside loop

# 2.continue - Skips the current iteration and moves to the next iteration of the loop.
for i in range(5):
    if i == 2:
        continue
    print(i)

# 0
# 1
# 3
# 4

# 3. pass - Does nothing; it is a placeholder where a statement is syntactically required but not implemented yet.
for i in range(5):
    pass


def function1():
    pass


class Test:
    pass


class Test1:
    ...