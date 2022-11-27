"""
in a class, the __init__ constructor assigns values to the attributes of the class and are executed as soon as a class
is executed

we can assign an attribute either by passing an arg or calculating the value in the initialisation
"""


class MyDummyClass:
    def __init__(self, a):
        self.a = a
        self.b = self.a * self.a

    def do_a_thing(self):
        # good showcase of how everything is an object. Even the tiniest attribute is a class
        return (
            f"the `b` object value is {self.b} the type is {self.b.__class__}, "
            f"the `a` object value is {self.a} the type is {self.a.__class__}"
        )


example = MyDummyClass(5)
print(example.a)
print(example.b)
print("calling custom method showcasing the class", example.do_a_thing())

"""
You can see in the example above, we have the, do a thing method which gives us some details on the object. 
However, we shouldn't need to create a custom method just to get the representative details of an object. 

We can instead use the __rep__ method to showcase what the class represents. We can then call it with the builtin repr()

You might be scratching your head thinking, why use this, but when you are working with large systems, you don't want
to have to learn numerous methods of how a class might try and represent itself and want universal tools
"""


class DummyClassWithDeets:
    def __init__(self, a):
        self.a = a
        self.b = self.a * self.a

    def __repr__(self):
        return f"DummyClassWithDeets(a={self.a}, b={self.b})"

    def __str__(self):
        output = (
            f"the `b` object value is {self.b} the type is {self.b.__class__}, "
            f"the `a` object value is {self.a} the type is {self.a.__class__}"
        )
        return output


print("standard representation method:", repr(DummyClassWithDeets(5)))

"""
You might also be wondering, what is the difference between __repr__ and __str__. Both can be called and both return
strings that assist with identifying the class. If you don't set the __str__ then it will just take the __repr__ value.

Repr is meant to return representation. It's more of a means to debug, rather than use 
"""
print("string  method:", str(DummyClassWithDeets(5)))

"""
Finally, there's __slots__. This is created on a class level

When we access the attributes of a class in python, the language runs the __getattribute__() method. This looks up the
self.__dict__["arg_name"] and returns the value

__slots__  allows us to explicitly declare data members and assigns a sequence of strings that are variable names

slots are more efficient in terms of memory space and speed of access but prevents us from using __dict__

The reason we might want this is because 
"""


class DummyClassWithSlots:
    __slots__ = ["a", "b"]

    def __init__(self, a):
        self.a = a


deet_class = DummyClassWithDeets(5)
slot_class = DummyClassWithSlots(5)
print("we can get the attributes like this", deet_class.a)
print(
    "which the attributes are in a dict",
    deet_class.__dict__.keys(),
    deet_class.__dict__.values(),
)
try:
    print(slot_class.__dict__)
except AttributeError as e:
    print(e, e.__traceback__)
print("However, slot class attribute access", deet_class.a)

# This can have some benefits as if you create
deet_class.c = 20
print("hey, this isn't in the original class!", deet_class.c)

try:
    slot_class.c = 20
    print(slot_class)
except AttributeError as e:
    print(e, e.__traceback__)

"""
I don't tend to use __slots__. The speed increase is very small and the dynamic creation of attributes is fine in almost
scenarios. 
"""