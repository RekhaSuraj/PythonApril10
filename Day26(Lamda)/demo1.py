# LEGB - Rules

# Local rule : Firstly, it check within that self, if the value doesn't find within that self it will go
# up next scope
# Hierarchy - order - LEGB - Scope order of a variable (Local, Enclosed, Global, BuiltIn)

prod = 'Iphone'
def greet():
    # prod = 'Phone'
    print(prod)

greet()
# Phone

# Iphone
