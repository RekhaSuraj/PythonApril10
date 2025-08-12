# lambda if else condition
# To find if a number is even or odd using lambda
x = lambda a:'even number' if a%2 == 0 else 'odd number'

print(x(6))
# even number

print(x(5))
# odd number

print(x(13))
# odd number

# lambda b: b%2 ==0 if 


# This can also be done
print('Even' if (lambda b: b % 2 == 0)(4) else 'Odd')  # Output: Even
print('Even' if (lambda b: b % 2 == 0)(5) else 'Odd')  # Output: Odd