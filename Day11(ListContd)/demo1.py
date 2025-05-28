list1 = ['hi','hello','welcome','world']
# insert() - Insert object before index

list1.insert(3,"GRK")
print(list1)
# ['hi', 'hello', 'welcome', 'GRK', 'world']

# sort() - Sort the list in ascending order and return None.
# If we dont specify any parameters inside the brackets, it arranges in ascending order by default
list1 = [5,2,1,6,9,10,33,11,22]

list1.sort()
print(list1)
# [1, 2, 5, 6, 9, 10, 11, 22, 33]

# If we want to arrange in descending order: reverse=True
list1.sort(reverse=True)
print(list1)
# [33, 22, 11, 10, 9, 6, 5, 2, 1]

# sorted() - Return a new list containing all items from the iterable in ascending order.
list2 = [55,22,66,33,10,11,88]
# sorted
li = sorted(list2)
print(li)
# [10, 11, 22, 33, 55, 66, 88]

print("list2",list2)
# list2 [55, 22, 66, 33, 10, 11, 88]

# TO sort in descending order
li1 = sorted(list2,reverse=True)
print(li1)
# [88, 66, 55, 33, 22, 11, 10]

# Key Differences:
# Feature	                    sort()	            sorted()
#
# Modifies original list?	    ✅ Yes	            ❌ No
# Returns new list?	            ❌ No	            ✅ Yes
# Works with lists only?	    ✅ Yes	            ❌ No (works with any iterable)
# Memory efficient?	            ✅ Yes	            ❌ No (creates new object)

# clear() - clears all the elements in the list and returns an empty list(Note: It does not delete the list)
list1.clear()
print(list1)
# [] #empty list