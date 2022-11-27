"""
In the equals methods, we overwrote the __eq__  method, however if we try to hash the value it errors
"""


class B:
    def __init__(self, v):
        self.v = v

    def __eq__(self, other):
        print(other.__dict__)
        return self.v == other.v


try:
    hash(B(10))
except TypeError as err:
    print(err, err.__traceback__)

"""
You might think, who cares?
Well, if we can't hash the values, we can't use it in a set
"""

try:
    val = {B(10)}
except TypeError as e:
    print(e, e.__traceback__)

dict_thing = {"test": B(10)}
list_thing = [B(10)]


"""
To resolve this, we need to overwrite the __hash__ method in the class. 
The python method __hash__ truncates the value returned from an object’s

__eq__ and __hash__ must agree - equal objects must have equal hashes. 
the __hash__ value should just return the hash function with an arg of the tuple
"""


class A:
    def __init__(self, v):
        self.v = v

    def __eq__(self, other):
        return self.v == other.v

    def __hash__(self):
        return hash((self.v, "test"))


print("function hash", hash(A("dummy")))
print("class method hash", A("dummy").__hash__())
print("see, hash method and the class method result in the same hash")

"""
As you can see, if you change the default __eq__ behaviour, you'll need to modify the __hash__ value
otherwise you'll come into issues later
"""
