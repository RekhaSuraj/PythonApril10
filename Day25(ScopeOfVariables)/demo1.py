# Scope of Variables:

# Understanding Scope
# In programming, the scope of a name defines the area of a program in which you can unambiguously access
# that name, such as variables, functions, objects, and so on.
# A name will only be visible to and accessible by the code in its scope.
# Several programming languages take advantage of scope for avoiding name collisions and unpredictable behaviors.


# There are four type's scopes
# 1.Local scope
# 2.Global scope
# 3.Enclosing scope(Nested function / closures)
# 4.Built-in Scope


# What is local variable ?
# A local variable is variable , which is defined inside the function, we access within the function

def greet():
    v1 = 'hello' # v1 is accessible only inside this function
    print('Local variable:',v1)

greet()
# Local variable: hello

# If we try to access local variable outside the function, we get the below Attribute error
# greet.v1
# AttributeError: 'function' object has no attribute 'v1'