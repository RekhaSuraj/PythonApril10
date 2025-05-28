# locals() - Return a dictionary containing the current scope's local variables.
# NOTE: Whether or not updates to this dictionary will affect name lookups in
#     the local scope and vice-versa is *implementation dependent* and not
#     covered by any backwards compatibility guarantees.

# print(help(locals))

def info():
    Name = 'Lakshmi'
    Age = 20
    Profession = 'IT'
    print(locals())
    # locals()['Age'] = 25
    Age = 25
    print(locals())
    print('Name:',locals()['Name'])


info()
# {'Name': 'Lakshmi', 'Age': 20, 'Profession': 'IT'}
# {'Name': 'Lakshmi', 'Age': 25, 'Profession': 'IT'}
# Name: Lakshmi

# print(locals())
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000002A04E5BBB90>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'F:\\Rekha\\GRKTrainings\\PythonApril10\\Day25(ScopeOfVariables)\\demo6.py', '__cached__': None, 'info': <function info at 0x000002A04E5AA2A0>}