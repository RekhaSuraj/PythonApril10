# List - Sequence datatype(inbuilt)
# List - 
# In python have some default Datatypes
# list is One of the Built in datatypes 

# list--> 
# collection of elements 
# it can be homogeneous(same datatype) or heterogeneous(different datatypes)
# each element is stored under a cell
# each cell has number--> index
# if list contains n number of elements then index will be 0 to n-1
# any index more than n-1 --> we get error out of range...

# to access element from list we use index --> listname[index]


#Why we are using list ?
# We can store Multiple different datatypes with in a single variable using the list.
# List have some unique methods, Append, remove
# using  above methods we can modify , Access the list value

# List is a Mutable datatype (Changeable) After creation
# List is a ordered collection of datatype (having a Unique index values) seperated by comma's
# List enclosed in Square brackets.

# string is immutable, whereas list is mutable

# ex1:syntax: listname = [list_elements]

list1 = [10,20,30,40,50] #homogeneous (same datatype)
print(type(list1))
# <class 'list'>

# To find the length of the list
print(len(list1))
# 5

# To create an empty list
list2 = []
print(list2)
# []


list3 = [20,40,5,6.5,4+5j,'hi','hello'] #heterogeneous (Different datatype)
print(type(list3))
# <class 'list'>

# Create a list using a constructor
l1 = list() # empty list 
print(l1)
# []

l2 = list([10,40,11,33,44,55,'hi'])
print(type(l2))
# <class 'list'>
print(l2)
# [10, 40, 11, 33, 44, 55, 'hi']