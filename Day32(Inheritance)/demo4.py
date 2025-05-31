# Single inheritance
class A:
    i = 10


class B(A):
    pass


obj_B = B()
print(obj_B.i)
# 10