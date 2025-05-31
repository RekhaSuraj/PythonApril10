# Multiple inheritance

class A:
    i = 10


class B:
    i = 20


class C(A,B):
    pass


print(C.i)
# 10
# print(C.j)

# 10
# 20

# If both parents have same variable, only the first parent's var will be considered. If we give below class C declaration,
# C.i will return 20
# class C(B,A):
#     pass