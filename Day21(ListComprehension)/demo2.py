# print positive and negative numbers in 2 separate lists
l1 = [10,-20,30,40,-50,60,-70,-80]
# pos_list = []
# neg_list = []
#
# for i in l1:
#     if i>0:
#         pos_list.append(i)
#     else:
#         neg_list.append(i)
#
# print(pos_list)
# print(neg_list)

# if condition - written at the end(list comprehension)
# List comprehension
p_list = [i for i in l1 if i>0]
print(p_list)
# [10, 30, 40, 60]

n_list = [j for j in l1 if j<0]
print(n_list)
# [-20, -50, -70, -80]