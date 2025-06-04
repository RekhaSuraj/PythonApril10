# Method overloading can be achieved using optional arguments like below:
class Overload_Opt:

    def Task(self,x,y=0,z=0):
        return x+y+z


obj_Overload = Overload_Opt()
print(obj_Overload.Task(10))
# 10

print(obj_Overload.Task(20,5))
# 25

print(obj_Overload.Task(5,10,15))
# 30
