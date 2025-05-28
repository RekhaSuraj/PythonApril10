# Type casting or conversion - if it is in int format
a = '10'
print('Before conversion:',type(a))
# Before conversion: <class 'str'>

# Conversion from string to int
b = int(a)
print(b)
print('After conversion:',type(b))
# After conversion: <class 'int'>

# Cannot convert alphabets into int
x = 'hello'
# y = int(x)
# print(y)
# ValueError: invalid literal for int() with base 10: 'hello'


