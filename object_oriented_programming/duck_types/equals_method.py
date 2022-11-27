import gc

# sortable
# iterator
# callable
# context manager (maybe there's something else we can do here different)

"""
Here's a funny thing, if you compare two different instances of the same class objects, you get False
"""


class A:
    def __init__(self, v):
        self.v = v


# What? Why?
print(A(10) == A(10))

"""
This is because when python compares two objects they compare the memory. As these two classes are different instances
== - for instance equality
is - for reference equality. This will only return true if they are the same memory address

However, we might want to compare classes by values, not by memory objects
__eq__ is called when python uses ==. It allows for one positional argument with one method, of v
"""


class B:
    def __init__(self, v):
        self.v = v

    def __eq__(self, other):
        print(other.__dict__)
        return self.v == other.v


b_one = B(10)
b_two = B(10)

print("Overwritten equal", b_one == b_two)

"""
In most instances, you want to use `is` to compare because some objects have the same memory
but the ability to overwrite this for == is useful

We can see all instance of a class by looking at the garbage collector
"""

for obj in gc.get_objects():
    if isinstance(obj, B):
        print(obj, obj.v)
