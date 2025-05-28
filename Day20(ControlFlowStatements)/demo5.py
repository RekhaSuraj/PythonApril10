# Duck number : Should not starts with zero, it contains of number at any palce
# Ex : 012345  (it's not duck number)
# Ex 120345 (its a duck number)

num = int(input('Enter a number :'))

Duck_num = False

while num != 0:
    digit = num % 10
    if digit == 0:
        Duck_num = True
        break  # Terminates the current loop Immediately
    num = num // 10

if Duck_num:
    print('Duck Number')

else:
    print('Not a Duck Number')
