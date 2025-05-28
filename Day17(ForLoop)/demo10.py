# Loop through a set
s1 = {10,20,30,40,50,60,'hi'}
for s in s1:
    print(s)
# 50
# hi
# 20
# 40
# 10
# 60
# 30
print()
# Loop through a dictionary:
# Print only keys
d1 = {1:'red',2:'blue',3:'pink',4:'black',5:'white'}

for k in d1:
    print(k)

# 1
# 2
# 3
# 4
# 5

print()
# Print only values from a dictionary
for v in d1:
    print(d1[v])

# red
# blue
# pink
# black
# white
print()
for k,v in d1.items():
    print(k,v)


# 1 red
# 2 blue
# 3 pink
# 4 black
# 5 white