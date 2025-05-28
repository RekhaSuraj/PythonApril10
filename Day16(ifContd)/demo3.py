# check if a string is palindrome

s1 = input('Please enter a string')

if s1 == s1[::-1]:
    print('Given string is a palindrome:',s1)
else:
    print('Given string is not a palindrome:',s1)

# Please enter a stringmom
# Given string is a palindrome: mom

# Please enter a stringmad
# Given string is not a palindrome: mad

# Please enter a string121
# Given string is a palindrome: 121

# Please enter a string1234
# Given string is not a palindrome: 1234