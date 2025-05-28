# Nested if

# Nested if-else statement
# In Python, the nested if-else statement is an if statement inside another if-else statement.
# It is allowed in Python to put any number of if statements in another if statement.
#
# Indentation is the only way to differentiate the level of nesting.
# The nested if-else is useful when we want to make a series of decisions.
#
# Syntax of the nested-if-else:
#
# if condition_outer:
#     if condition_inner:
#         statement of inner if
#     else:
#         statement of inner else:
#
# else:
#     Outer else
# statement outside if block

# Program to check even or odd
n1 = int(input('Enter a number'))
if n1 > 0: #outer if condition
    if n1 % 2 == 0: #inner if condition
        print('Number is even',n1) #statement of inner if
    else: #inner else
        print('Number is odd',n1) #statement of inner else
else: # outer else
    print('Invalid input') #outer else statement

# Enter a number8
# Number is even 8

# Enter a number5
# Number is odd 5

# Enter a number0
# Invalid input

# Enter a number-4
# Invalid input