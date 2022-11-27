"""
all attributes are public in python, so we can set or get them at any time. If we modify the property directly like
MyDummyClass.a = 10
we are access the property directly and can overwrite logic or arguments in the class instance. This can break methods
and there's no warning.

Maybe we don't want this behaviour, so we make an attribute protected and validate then by using a getter and setter.
getter - returns the value of the attribute
setter - sets the value of the attribute
deleter - deletes the value of the attribute

This can make things complicated because if we build custom getter and setter methods, every method is going to need
run custom logic checks to make sure someone hasn't changed the attribute to say a negative number or something that
breaks your methods.

Instead, we can use the @property decorator. @property is a special decorator to make a method act as a getter, setter
or deleter.

As someone who doesn't usually care all that much about if an object is private or not, the best argument for
@properties is the ability to perform checks on the attributes and log changes to the console
"""


class PropertyClass:
    def __init__(self, a):
        self._a = a
        self.b = self._a * self._a

    @property
    def a(self):
        print("getter of a called")
        return self._a

    @a.setter
    def a(self, new_val):
        # you might notice that the setter, deleter and getter all have the same name
        print(f"setting new val: {new_val}")
        self._a = new_val

    @a.deleter
    def a(self):
        print("a has been deleted")
        del self._a


print(
    "you might be thinking, why use a property, you can get the same value by calling the property"
)
print(
    "getter, setter called on declaration", PropertyClass(5).a
)  # the printout shows the getter and setter called
print("protected attribute can still be obtained", PropertyClass(5)._a)
print(
    "having the ability to still get the protected attribute is useful"
    "but it having a getter/setter tells the user to go through the proper channels"
)

declared = PropertyClass(10)
print("maybe you are feeling lazy and don't want to use properties")
print("b is:", declared.b)
declared.b = 5
print("b is now:", declared.b)
print(
    "oh, the property was changed and when looking at the console, we have no idea why"
)

print("We can still modify the attribute value directly: before", declared.a)
declared._a = 100
print("protect value overwrite", declared.a)

print("let's clear things up and delete the property")
del declared.a
print("nice, attribute a is gone")

try:
    print(declared.a)  # notice how the getter is still called but nothing is found
except AttributeError as e:
    print(e, e.__traceback__)
declared.a = 10
print("however, we can set the value again cleanly", declared.a)

print("trying to do the same with b is possible")
del declared.b
declared.b = 110
print(
    "however, there's no indication what made the changes to the attribute or if it breaks any methods:",
    declared.b,
)
# properties are cool, but I feel like they are badly explained and under utilised by many engineers
