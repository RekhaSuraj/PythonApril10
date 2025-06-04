from multipledispatch import dispatch
class Arithmetic:

    @dispatch(int,int)
    def Task(self,x,y):
        return x+y

    @dispatch(int,int,int)
    def Task(self,x,y,z):
        return x+y+z

    @dispatch(int,int,int,int)
    def Task(self,x,y,z,l):
        return x+y+z+l


obj_arithmetic = Arithmetic()
print(obj_arithmetic.Task(10,20))
# 30

print(obj_arithmetic.Task(5,2,1,3))
# 11

print(obj_arithmetic.Task(10,2,5))
# 17

