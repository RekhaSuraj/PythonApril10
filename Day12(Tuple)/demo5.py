import sys
list1 = [40,30,20,50,60,80,100]
print(len(list1))
# 7
t1 = (40,30,20,50,60,80,100)
print(len(t1))
# 7

# sys.getsizeof() - Return the size of object in bytes
print(sys.getsizeof(list1)) # More memory size
# 120
print(sys.getsizeof(t1)) # Less memory size
# 96


# 3. Syntax Differences
# Feature	    List	                            Tuple
# Declaration	my_list = [1, 2, 3]	                my_tuple = (1, 2, 3)
# Mutability	Mutable (Changeable)	            Immutable (Not changeable)
# Performance	Slower (More Memory)	            Faster (Less Memory)
# Methods	    More (e.g., append(), remove())	    Fewer (Only count(), index())
# Use Cases	    When data changes often	            When data remains fixed