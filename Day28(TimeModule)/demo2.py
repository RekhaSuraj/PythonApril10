import time
#     %Y  Year with century as a decimal number.
#     %m  Month as a decimal number [01,12].
#     %d  Day of the month as a decimal number [01,31].
#     %H  Hour (24-hour clock) as a decimal number [00,23].
#     %M  Minute as a decimal number [00,59].
#     %S  Second as a decimal number [00,61].
#     %z  Time zone offset from UTC.
#     %a  Locale's abbreviated weekday name.
#     %A  Locale's full weekday name.
#     %b  Locale's abbreviated month name.
#     %B  Locale's full month name.
#     %c  Locale's appropriate date and time representation.
#     %I  Hour (12-hour clock) as a decimal number [01,12].
#     %p  Locale's equivalent of either AM or PM.

# In a readable format
t1 = time.strftime('%Y-%m-%d %H-%M-%S')
print(t1)
# 2025-05-26 14-17-07

print(time.strftime('%a-%A-%b-%B-%c-%I'))
print(time.strftime('%c'))
print(time.strftime('%I'))
print(time.strftime('%p'))