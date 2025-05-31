# Multilevel inheritance:
class A:
    i = 10


class B(A):
    pass


class C(B):
    pass


print(C.i)
# 10
print(B.i)
# 10