"""
The __call__ method can be used to turn the instances of the class into callables. Functions are callable objects
by defining the __call__ method for a class, we can

this is done by using the `callable which checks if the object is callable or not
"""


class B:
    def __init__(self, v):
        self.v = v


beep = B(10)
try:
    print(beep())
except TypeError as e:
    print(e, e.__traceback__)

print("interesting, let's see. Is it callable?", callable(beep))


class A:
    def __init__(self, v):
        self.v = v

    def __call__(self):
        return f"{self.v} is the value we are calling"


thing = A(10)
print("Is this callable?", callable(thing), thing())
