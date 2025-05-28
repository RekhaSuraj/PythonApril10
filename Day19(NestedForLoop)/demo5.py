# print first 5 even numbers using while loop
i = 1
cntr = 0
while cntr < 5:
    if i % 2 == 0:
        print(i)
        cntr += 1
        # print('cntr',cntr)
    # print('before inc:i',i)
    i = i+1
    # print('after inc:i',i)

# 2
# 4
# 6
# 8
# 10


# before inc:i 1
# after inc:i 2
# 2
# cntr 1
# before inc:i 2
# after inc:i 3
# before inc:i 3
# after inc:i 4
# 4
# cntr 2
# before inc:i 4
# after inc:i 5
# before inc:i 5
# after inc:i 6
# 6
# cntr 3
# before inc:i 6
# after inc:i 7
# before inc:i 7
# after inc:i 8
# 8
# cntr 4
# before inc:i 8
# after inc:i 9
# before inc:i 9
# after inc:i 10
# 10
# cntr 5
# before inc:i 10
# after inc:i 11

# hw : print first 10 odd numbers using while loop