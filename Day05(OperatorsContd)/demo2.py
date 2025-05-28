# Identity operator - is, is not

# works on only iterables(list,tuple,set,dict)
# There are two Identity Operators  : 1).is, 2). is not
# is - returns True if both objects are same (both have same id)

# syntax : id(object) - Returns address or id of the object inside the brackets
a = 10
print(id(a))
# 140733444012760

b = 20
print(id(b))
# 140733444013080

print(a is b)
# False

c = 10
print(id(c))
# 140733444012760

print(a is c)
# True

list1 = [10,20,30]
list2 = [10,20,30]

print(list1 is list2)
# False

print('list1',id(list1))
print(id(list2))
# list1 2233353884032
# 1938182756544

list3 = list1
print(list1 is list3)
print('list3',id(list3))
# list3 2233353884032
# True