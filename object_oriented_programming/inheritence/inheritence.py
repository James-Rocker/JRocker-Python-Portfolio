"""
Inheritance is a useful programming concept that allows classes to inherit methods and properties from other classes

We can then separate classes by parents and child
"""


class A:
    def __init__(self, v):
        self.v = v

    def print_out(self):
        print(self.v)


class AChild(A):
    pass


print(AChild(5).print_out())

"""
As you can see, even though the AChild class doesn't call for an argument, it is needed because the parent class
requires one and the child can use methods from the parent class 

What happens with adding an __init__ method on the child class?
"""


class AChildInit(A):
    def __init__(self, beep, boop):
        self.beep = beep
        self.boop = boop


try:
    print(AChildInit(1, 2).print_out())
except AttributeError as err:
    print(err, err.__traceback__)


"""
Oh, because we have overwritten the initialisation from the parent. This is cool but it does mean, any method that the
parent class uses that required initialised attributes might raise and AttributeError. 

We can get around this by either, calling the parent class init but I'm not a fan of that
Or we can use the super method. This allows the child to receive all attributes from the parent
"""


class SecondAChildInit(A):
    def __init__(self, beep, boop, v):
        A.__init__(self, v)
        self.beep = beep
        self.boop = boop


SecondAChildInit(1, 2, 5).print_out()


class ThirdAChildInit(A):
    def __init__(self, beep, boop, v):
        super().__init__(v)
        self.beep = beep
        self.boop = boop


ThirdAChildInit(1, 2, 5).print_out()
