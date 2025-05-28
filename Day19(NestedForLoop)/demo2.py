# pattern printing

# square
for i in range(3):
    for j in range(3):
        print('*',end=' ')

    print() #goes to next line

# * * *
# * * *
# * * *
print('-------------------')
# Rectangle pattern:
for i in range(4):
    for j in range(3):
        print('*',end=' ')

    print()

# * * *
# * * *
# * * *
# * * *

print('-----------------')
# right angled triangle
for i in range(1,5):
    for j in range(i):
        print('*',end=' ')

    print()

# i=0
# j=0
#
# i = 1
# j = 0
#
# i = 2
# j = 0,1
#
# i = 3
# j = 0,1,2,

# *
# * *
# * * *
# * * * *

print('-----------------')
# hw - reverse right angled triangle

# 1 2 3
# 4 5 6
# 7 8 9

cntr = 1
for i in range(3):
    for j in range(3):
        print(cntr,end=' ')
        cntr = cntr+1

    print()

# 1 2 3
# 4 5 6
# 7 8 9