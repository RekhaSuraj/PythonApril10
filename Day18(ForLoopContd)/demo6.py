# Count the number of characters in a string
str1 = 'HellHo World'

# {'H':1,'e':1,'l':3,'o':2,'W':1,'r':1,'d':1}

char_dict = {}
for s in str1:
    if s in char_dict:
        char_dict[s] = char_dict[s] + 1

    else:
        char_dict[s] = 1

print(char_dict)

# {'H': 2, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'W': 1, 'r': 1, 'd': 1}

# print only duplicates values in the dictionary:
dup_dict={}

for k in char_dict:
    if char_dict[k] > 1:
        dup_dict[k] = char_dict[k]

print(dup_dict)
# {'H': 2, 'l': 3, 'o': 2}

# H
# char_dict['H'] = 1

# e
# char_dict['e'] = 1


# l
# char_dict['l'] = 1
# char_dict['l'] = char_dict['l'] +1
# char_dict['l'] = 1 + 1
# char_dict['l'] = 2


# o
# char_dict['o'] = 1

# W
# char_dict['W'] = 1

# o
# char_dict['o'] = char_dict['o'] +1
# char_dict['o'] = 1+1
# char_dict['o'] = 2

# r
# char_dict['r'] = 1

# l
# char_dict['l'] = 2
# char_dict['l'] = char_dict['l'] + 1
# char_dict['l'] = 2 + 1
# char_dict['l'] = 3


# d
# char_dict['d'] = 1


# hw
# Print only non duplicate values in the dictionary

