# Find factorial using return keyword
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i

    return fact


res = factorial(int(input('Enter a number')))
print(res)
# Enter a number5
# 120
