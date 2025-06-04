# Method Overloading

class Test:

    def speed(self,x):
        print(x)

    def speed(self,x,y):
        print(x,y)


obj_test = Test()
# Only latest method will be called
# obj_test.speed(4,5)

# If I try to call the method with single parameter, we will get the below error
# obj_test.speed(5)
# TypeError: Test.speed() missing 1 required positional argument: 'y'