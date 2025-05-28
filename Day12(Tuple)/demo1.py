# Tuple - Sequence Datatype
# Tuple is a Built-in datatype in python
# It is used to store multiple values with in a single unit to Assign to a variable name
# Tuple denoted by round braces / Parenthesis  ( )
# It can have items of any datatype. It can be heterogeneous or homogeneous
# Imp: Tuple is immutable (Cannot be changed after creation)

# There are two ways to create a tuple
# Type : 1  using the Parenthesis

t1 = (10,20,30,40,50)
print(type(t1))
# <class 'tuple'>

# Type : 2 using constructor
t2 = tuple((10,30,50,60,70.5,'hi','hello'))
print(type(t2))
# <class 'tuple'>

# Creating an empty tuple
t3 = tuple()
print(type(t3))
# <class 'tuple'>

t4 = ()
print(type(t4))
# <class 'tuple'>