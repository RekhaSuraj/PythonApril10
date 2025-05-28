# Write a program for taking pwd input from user, if wrong pwd for 3 attempts, then account gets locked

# 1234
pwd = int(input('Enter password'))
attempts = 1

while attempts != 3:
    if pwd == 1234:
        print('Access granted')
        break

    else:
        print('Wrong password')
        pwd = int(input('Enter password again'))

    attempts += 1
    print(attempts)

else:
    print('Access blocked - exceeded 3 attempts')


# Enter password1234
# Access granted


# Enter password23
# Wrong password
# Enter password again45
# 2
# Wrong password
# Enter password again56
# 3
# Access blocked - exceeded 3 attempts

