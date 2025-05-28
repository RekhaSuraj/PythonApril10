v1 = 100
def sum_function():
    v1 = 200
    print(f'LocalVar:{v1}')
    print(f'GlobalVar:{globals()['v1']}')
    sum1 = globals()['v1']+v1
    print(sum1)


sum_function()

# LocalVar:200
# GlobalVar:100
# 300