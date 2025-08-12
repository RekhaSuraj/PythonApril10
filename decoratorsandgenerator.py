def outer_fun(name):

    def inner_fun():
        # v1 = name()
        return name().upper()

    return inner_fun

@outer_fun
def get_data():
    return 'hello world how are you'


print(get_data())


def out_fun(msg):

    def inner_fun():
        m = msg()
        return f'hello, good morning {m}'

    return inner_fun


@out_fun
def birthday():
    return 'Rama'


print(birthday())

# generator
def gen_fun():
    yield 10
    yield 20
    yield 30
    yield 40
    yield 50


obj_gen = gen_fun()
print(next(obj_gen))
print(obj_gen.__next__())

print()
for i in obj_gen:
    print(i)

print()
# iterators
# An iterator is any object in Python that implements the __iter__() and __next__() methods.
# ✅ Characteristics:
# Can be used in a for loop.
# Remembers its state between iterations.
# Raises StopIteration when items are exhausted.
# ✅ How to create:
# You can create an iterator from any iterable (like a list, tuple, string) using the iter() function.

nums = [10,20,30,40,50]
it = iter(nums)

print(next(it))
print(next(it))

for i in it:
    print(i)


# print(next(it))
# StopIteration

# Feature	            Iterator	                                                Generator
# How it's created	Using a class with __iter__() and __next__()	            Using a function with yield or a generator expression
# Simplicity	        Requires more boilerplate code	                            Very concise and readable
# Memory efficiency	May store all elements in memory	                        Yields one value at a time (lazy)
# Example	            iter([1, 2, 3])	                                            def gen(): yield 1
