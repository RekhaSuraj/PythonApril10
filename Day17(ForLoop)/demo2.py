# simple atm program

balance = 2000
amount = int(input('Enter the amount to be withdrawn'))

if amount < balance:
    print('Transaction successful')
    balance = balance - amount
    print('Your new balance is:',balance)

else:
    print('Insufficient balance')

# Enter the amount to be withdrawn500
# Transaction successful
# Your new balance is: 1500

# Enter the amount to be withdrawn2500
# Insufficient balance