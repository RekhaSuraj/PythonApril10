s = {10,20,30,40,50,60}
s1 = {10,20,30}

# issuperset() - Report whether this set contains another set
print(s.issuperset(s1))
# True

# issubset() - Report whether another set contains this set
print(s1.issubset(s))
# True

print(s.issubset(s1))
# False