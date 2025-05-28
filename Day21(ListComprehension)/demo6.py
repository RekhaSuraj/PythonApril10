# Replace negative numbers with 0 using list comprehension
li1 = [10,-20,30,-4,-5,8,-9]

cnt_elements = len(li1)
for j in range(cnt_elements):
    if li1[j] < 0:
        li1[j] = 0

print(li1)
# [10, 0, 30, 0, 0, 8, 0]

# using list comprehension:
new_list = [j if j>0 else 0 for j in li1]
print(new_list)
# [10, 0, 30, 0, 0, 8, 0]


li = [10,-20,30,-4,-5,8,-9]

# Prints only negative numbers
n_list = [j for j in li if j<0]
print(n_list)
# [-20, -4, -5, -9]




