from enum import Enum

"""
an enumerate is a set of symbolic names bound to unique values.

these are immutable data types. They can be useful for creating constants in a class format e.g. days of the week or 
colours
"""


class Colours(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(Colours.BLUE)  # printing just the attribute doesn't show the value of the attributes
print(repr(Colours.BLUE))  # getting representation gives the value but it's not ideal
print(Colours.BLUE.name, Colours.BLUE.value)  # we can instead get the name and value of the attribute similar to dicts
