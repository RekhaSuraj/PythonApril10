# double all numbers in a list using HOF

list1 = [3,2,5,8,6,10]

def double_num(n):
    return n+n

print(tuple(map(double_num,list1)))
# (6, 4, 10, 16, 12, 20)

# using lambda
print(list(map(lambda n:n+n,list1)))
# [6, 4, 10, 16, 12, 20]

