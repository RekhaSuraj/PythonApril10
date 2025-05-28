# find the biggest number in a list without using max() inbuilt method

list1 = [10,4,20,15,26,45,38,19]

# Using max()
# print(max(list1))
# 45

big = list1[0] #10
cnt = len(list1)

for i in range(cnt):
    if list1[i] > big:
        # print('list item',list1[i])
        # print('before big',big)
        big = list1[i]
        # print('after update',big)

print('Biggest number:',big)
# Biggest number: 45


# list item 20
# before big 10
# after update 20
# list item 26
# before big 20
# after update 26
# list item 45
# before big 26
# after update 45


# hw:
# Find smallest number in this list without using min() inbuilt method
print(min(list1))