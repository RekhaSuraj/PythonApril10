from contextlib import contextmanager


@contextmanager
def my_context():
    print("Setup")
    yield
    print("Cleanup")


with my_context():
    print("Inside the with block")
