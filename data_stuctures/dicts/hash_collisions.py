import string

"""
Python is able to handle large strings and work with them quickly. This is the same for all sequence objects
including strings, list, and tuples.
This can be great for objects that will get really large
"""

upper_string = (
    string.ascii_uppercase * 100_000_000
)  # built a 2.6 billion list of upper_case strings

# just printing upper_string takes a long time, however, getting the object locations is still quick
print(
    "first 26:",
    upper_string[:26],
    "last 26:",
    upper_string[-26:],
    "middle value:",
    upper_string[len(upper_string) // 2],
)
print(len(upper_string))

"""
this is because python uses a random-access structure. The way I like to think of it is, like a book where you can
open to any page. While say a scroll is sequential which is done through sequential access.

to quote the real-python hash-tables article
The array occupies a contiguous block of memory.
Every element in the array has a fixed size known up front.

a hash table is a data structure that allows you to store a collection of key-value pairs (or hash table)
the difference between this and a dict is every value must be hashable. While a dict is key, value pairing

so, what happens when something has the same hash value?
"""


class A(object):
    def __hash__(self):
        return 42


print(A())
print(A())


class B(object):
    def __eq__(self, other):
        return True


class C(A, B):
    pass


dict_a = {A(): 1, A(): 2, A(): 3}
dict_c = {C(): 1, C(): 2, C(): 3}

# oh, we can see the different keys are given different hash values
print(dict_a)
print(dict_c)

"""
Python dicts uses open addressing. Each key, value is stored into a list (or bucket) of elements at the hash
then iterates through that list until it finds the actual key in that list
"""
