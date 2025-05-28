# Filter - HOF
#syntax: filter(function_name,iterable)

# generate even numbers from 0 to 20
def even_nos(num):
    # if num%2 == 0:
    return num%2 == 0

print(list(filter(even_nos,range(21))))
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# using lambda
print(list(filter(lambda a: a%2 ==0,range(21))))
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# hw - Print names that start with 'A'
# list2 = ['Welcome','Ajay','Arjun','Pooja','Amar']

