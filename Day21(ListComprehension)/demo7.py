# Add 1 to all elements in the list
l1 = [10,20,30,40,50]
new_list=[]
for i in l1:
    new_list.append(i+1)

print(new_list)
# [11, 21, 31, 41, 51]

# using list comprehension
n_list = [i+1 for i in l1]
print(n_list)
# [11, 21, 31, 41, 51]

# Remove duplicates from a list - hw
# odl_list = [11,3,45,22,6,-4,2,6,4,2,4,6,0,12]