# In Python, a while loop can have an else clause.
# The else block executes only if the loop completes normally (i.e., without encountering a break)

# while condition:
#     # Loop body
# else:
#     # Executes if the loop runs to completion (condition becomes False)
#
# Example 1: while with else (Normal Execution)
i = 1
while i <= 3:
    print(i)
    i = i+1

else:
    print('Loop executed normally')

# 1
# 2
# 3
# Loop executed normally

# Example2: while with break (Else Skipped)

i = 1
while i <= 3:
    print(i)
    if i == 2:
        break
    i = i+1

else:
    print('else block:executed normally')
#
# 1
# 2

