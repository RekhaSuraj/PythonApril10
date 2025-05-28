# Write a program to check if a number is prime or not

num1 = int(input('Enter a number'))
is_prime = True
for i in range(2,num1):
    if num1 % i == 0:
        is_prime = False
        break

if is_prime == True:
    print(num1,'is a prime number')
else:
    print(num1,'not a prime number')

# Enter a number5
# 5 is a prime number

# Enter a number4
# 4 not a prime number

# Enter a number9
# 9 not a prime number

# Enter a number7
# 7 is a prime number