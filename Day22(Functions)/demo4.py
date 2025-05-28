# To pass Parameters when you defining function

# syntax : def functionname(para1,para2,........ParaN):
#                 body of function
#
#functionname(Arg1,Arg2,...........AgrN)


# Function definition: or function declaration
def add(num1,num2):
    print('Addition of values:',num1+num2)

# calling the function:
# add()
# TypeError: add() missing 2 required positional arguments: 'num1' and 'num2'

# add(10)
# TypeError: add() missing 1 required positional argument: 'num2'

add(10,20)
# Addition of values: 30