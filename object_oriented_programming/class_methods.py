from random import randint

"""
You might have looked at the other classes we are using in different scripts and wonder, why are we using self?
self - instance methods for accessing attributes
cls - class methods for accessing the class itself 

You could also use cls which refers to the class instance 
"""


class MyMethodClass:
    def method(self):
        return "instance method called", self

    @classmethod
    def class_method(cls):
        return "class method called", cls

    @staticmethod
    def static_method():
        return "static method called"


print(MyMethodClass.method)
print(MyMethodClass.class_method())
print(MyMethodClass.static_method())

"""
Within a class, you have methods. These are functions within the class that modify object values. There are different
types of methods though, instance methods, class methods and static methods

instance methods
uses the `self` instance of the class allowing it to get class attributes modify class state. I won't demo them here
as I have used them frequently throughout the repo. 99% of my programming time has just been used to make this 

class methods
accepts cls and points directly to the class. For example when you are trying create multiple pieces of logic for a
constructor. You could just create the attribute with 
self.x = none 
then give the value later or make class methods to manipulate 

static methods
static methods don't modify the class or the state. I find most of the time, they are better as generic functions but
sometimes it's useful to glue functions together or breakdown a function. It's sometimes useful for encapsulating
generic logic within single class but that's more preference. 
"""


class Cheese(object):
    # taken from https://stackoverflow.com/a/682545/12201158
    def __init__(self, num_holes=0, another_arg=None):
        # defaults to a solid cheese
        self.number_of_holes = num_holes
        self.another_arg = another_arg

    @classmethod
    def random(cls):
        return cls(randint(0, 100), "hello")

    @classmethod
    def slightly_holey(cls):
        return cls(randint(0, 33))

    @classmethod
    def very_holey(cls):
        return cls(randint(66, 100))


cheese = Cheese()
another_cheese = Cheese.random()
print(
    another_cheese.__repr__(),
    another_cheese.number_of_holes,
    another_cheese.another_arg,
)

slightly_holey_cheese = Cheese.slightly_holey()
print(
    slightly_holey_cheese.__repr__(),
    slightly_holey_cheese.number_of_holes,
    slightly_holey_cheese.another_arg,
)

very_holey_cheese = cheese.very_holey()
print(
    very_holey_cheese.__repr__(),
    very_holey_cheese.number_of_holes,
    slightly_holey_cheese.another_arg,
)
print(
    "As you can see, these are all cheese objects but it allows the class to have built in logic for the arguments"
)
