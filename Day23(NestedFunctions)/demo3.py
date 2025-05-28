# even odd using return keyword

def even_odd(num):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'


res = even_odd(int(input('Enter a number')))
print(res)

# Enter a number4
# Even

# Enter a number9
# Odd