# Check for username and pwd from user

un = input("Please enter a username")
pwd = int(input('Please enter a password'))

if un == 'python' and pwd == 1234:
    print('Access granted')
else:
    print('Access blocked')

