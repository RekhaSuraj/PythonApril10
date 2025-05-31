# Hierarchial Inheritance
class A:
    i = 20

class B(A):
    pass

class C(A):
    pass

print(C.i)
print(B.i)

# 20
# 20