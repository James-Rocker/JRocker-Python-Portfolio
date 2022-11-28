"""
Lets you want to iterate over something (an iterable being something you can loop over). To do this, we pass an
iterable object to the iter() built-in python method which returns an iter object of the object. This uses the
__iter__ object method.

Say you have a custom class, and you want to iterate over it using the same method. Out of the box we can't
"""

a_list = [2, 7, 9, 3]
an_iter = iter(a_list)
print(type(an_iter))
print("first call of iterator", next(an_iter))
print("second call of iterator", next(an_iter))
a_set = {1, 2, 3, 4}
another_iter = iter(a_set)
print(type(another_iter))


class A:
    def __init__(self, v):
        self.v = v


try:
    print(iter(A(a_list)))
except TypeError as err:
    print(err, err.__traceback__)

"""
Cool, so we have to define the __iter__ method on that class. Within the iter, we need to store the index within an
attribute e.g. `self.x`

We also have to implement __next__ as well so the iterator
can pass next to it.

Within the __next__ method, we need to make sure there is that means to `raise StopIteration` otherwise the iterator
could be run forever.
"""


class B:
    def __init__(self):
        self.v = 1

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        result = 2 ** self.n
        self.n += 1
        return result


iter_class_b = iter(B())
for each in range(100):
    if each == 99:
        print("Cool, we can iterate for as long as we like!", next(iter_class_b))
    else:
        next(iter_class_b)


"""
However, we might not want to have the iterator run forever. In that event, we can apply some logic and use the 
raise StopIteration
"""


class C:
    def __init__(self):
        self.v = 1

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.v:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            print("iteration number is", self.v, "value is", self.v)
            raise StopIteration


iter_class_c = iter(C())
for each in range(10):
    try:
        next(iter_class_c)
    except StopIteration as err:
        print(f"Cool, we can't run forever and fails on the loop call {each}, run {err.__traceback__}")
        break
