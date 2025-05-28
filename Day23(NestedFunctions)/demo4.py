def prime_no(num):
    msg = 'Prime'
    for i in range(2,num):
        if num % i ==0:
            msg = 'NotPrime'
            break

    return msg

n1 = int(input('Enter a number'))
res = prime_no(n1)
if res == 'Prime':
    print(f'{n1} is Prime')
else:
    print(f'{n1} is not Prime')


# Enter a number7
# 7 is Prime


