# print even and odd numbers in 2 separate list
list1 = [12,3,14,6,8,23,15,17,19,32]

even_list=[]
odd_list = []
for i in list1:
    if i % 2== 0:
        even_list.append(i)

    else:
        odd_list.append(i)


print('Even List',even_list)
print('Odd List',odd_list)

# Even List [12, 14, 6, 8, 32]
# Odd List [3, 23, 15, 17, 19]


