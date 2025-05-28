# print all positive and negative numbers in 2 separate lists
list1 = [10,20,-30,50,-60,-70,70,-80]

pos_list = []
neg_list = []
for i in list1:
    if i > 0:
        pos_list.append(i)

    else:
        neg_list.append(i)


print('Positive list',pos_list)
print('Negative list',neg_list)

# Positive list [10, 20, 50, 70]
# Negative list [-30, -60, -70, -80]
