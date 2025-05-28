def greet(name):
    def message():
        return f'Hello {name}'

    return message() # Inner function uses the variable from the outer function


print(greet('Lakshmi'))
# Hello Lakshmi


def outer_sum(n1,n2,n3):
    sum_outer = n1+n2+n3 #60

    def inner_sum(num1,num2,num3):
        sum_inner = num1+num2+num3 #6
        return sum_inner

    v1 = inner_sum(1,2,3)
    return v1 + sum_outer


print(outer_sum(10,20,30))
# 66

# hw - using functions using return
# largest number in a list without using max()
# Smallest number in a list without using min()
# Length of a list without using len()
# prime number