# Hybrid Inheritance

class A:
    i = 10

class B:
    j = 20

class C(A,B):
    pass

class D(C):
    pass

class E(C):
    pass


print(C.i)
print(C.j)
# 10
# 20

print(D.i)
print(D.j)

# 10
# 20