# Enclosing Scope: Nested functions

# Enclosing (or nonlocal) scope is a special scope that only exists for nested functions.
# If the local scope is an inner or nested function, then the enclosing scope is the scope of the
# outer or enclosing function.
# This scope contains the names that you define in the enclosing function.
# The names in the enclosing scope are visible from the code of the inner and enclosing functions.
# Enclosing variable declared Inside the outer function, Outside the inner function

x = 10 #Global Var
print(f'GlobalVar:{x}')
def outer_fun():
    v1 = 100 #Enclosed variable
    def inner_fun():
        v2 = 200 #Local
        print('LocalVar:',v2)
        print('EnclosedVar:',v1)

    inner_fun()
    print('EnclosedVar:',v1)

outer_fun()
# Accessing Enclosing var outside the function will give NameError like below:
# print(f'EnclosedVar:{v1}')
# NameError: name 'v1' is not defined



