# return statement

# Return Value From a Function
# In Python, to return value from the function, a return statement is used.
# It returns the value of the expression following the return keyword.
#
# Syntax of return statement
#
# def fun():
#     statement-1
#     statement-2
#     statement-3
#     .
#     .
#     return [expression]
# The return value is nothing but a outcome of function.
#
# The return statement ends the function execution. Once a function encounters a return statement, execution comes out(Code
# written after return statement will not be executed.
# For a function, it is not mandatory to return a value.
# If a return statement is used without any expression, then the None is returned.
# The return statement should be inside of the function block.


def foo():
    return "Greetings from GRK School"

# print(foo())
a = foo()
print(a)
# Greetings from GRK School
