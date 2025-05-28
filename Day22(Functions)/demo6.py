# Write a program to check if a number is even or odd using function
def even_odd(num):
    if num % 2 == 0:
        print(f'{num} is even number')
    else:
        print(f'{num} is odd number')


even_odd(6)
# 6 is even number

even_odd(5)
# 5 is odd number

# taking input from user
# n2 = int(input('Enter a number'))
# even_odd(n2)

even_odd(int(input('Enter a number')))
# Enter a number7
# 7 is odd number

# Enter a number10
# 10 is even number