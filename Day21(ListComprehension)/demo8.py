# fibonacci numbers
first = 0
second = 1
next = 0
print(first,second,end=' ')

for i in range(1,10):
    next = first+second
    print(next,end=' ')
    first = second
    second = next

# 0 1 1 2 3 5 8 13 21 34 55