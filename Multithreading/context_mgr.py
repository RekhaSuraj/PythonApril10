class MyContext:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")


with MyContext() as ctx:
    print("Inside the with block")


# a & = 10

x = 20
y = 'hello'
z = 4.5


