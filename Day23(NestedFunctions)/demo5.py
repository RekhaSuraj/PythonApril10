# Nested functions
# A nested function is a function defined inside another function

def outer_function():
    print("This is the outer function.")

    def inner_function():
        print("This is the inner function.")

    print('Before calling inner_function')
    inner_function()  # Calling the inner function inside the outer function4
    print('After calling inner_function')


print('Before calling outer_function')
outer_function()
print('After calling outer function')

# Before calling outer_function
# This is the outer function.
# Before calling inner_function
# This is the inner function.
# After calling inner_function
# After calling outer function

