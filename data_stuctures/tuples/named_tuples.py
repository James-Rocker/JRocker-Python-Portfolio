from collections import namedtuple

# named tuples are part of the collections' library. They act as classes for tuples (also immutable)
# you provide the object name and then the fields names
Point = namedtuple("Point", "x y")
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)
print(pt1)

# we can unpack the values
x, y = pt1
print(x)
