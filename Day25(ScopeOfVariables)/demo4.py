# Updating the global variable
# Updates to this dictionary *will* affect name lookups in the current
# global scope and vice-versa.


v1 = 100
print(f'Global Var:{v1}')
def profile():
    v1 = 200
    print(f'Local Var:{v1}')
    print(f'Global Var:{globals()['v1']}')
    globals()['v1'] = 500
    print(f'Updated GLobalVar:{globals()['v1']}')


profile()
print(globals()['v1'])

