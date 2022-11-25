import array as arr

"""
an array is a collection of items
arrays are similar to lists. They are ordered, mutable, able to store repeats and are even in square brackets

However lists are flexible and can store multiple types, while an array can only store a single type
"""

array_1 = arr.array("i", [1, 2, 3, 4])
print(array_1)
print(type(array_1))

"""
so, what's the point?

arrays can store large amounts of data and work well for mathematical operations
arrays act as a wrapper for the C level of arrays. However, most of the time when working with arrays,
it will be through the numpy library
"""

import numpy as np

new_array = np.array([1, 2, 3])
print((new_array / 2).tolist())  # this allows us to divide all objects incredibly quickly

# this also allows you to make 2-d arrays
two_d_array = np.array([[1, 2, 3], [4, 5, 6]])

# here you can perform various actions to it easily
print(two_d_array.shape)  # 2 lists, with 3 corresponding objects in each
print(two_d_array.dtype)  # what object types they contain
print(two_d_array.size)  # how many objects

# we can even make 3 dimensional arrays
three_d_array = np.array([[1, 2, 3], [4, 6, 2], [0, 7, 1]])
print(three_d_array.size)  # which allows you to do additional actions

# you can pass strings to an array
string_array = np.array(["hello", "world"])
print(type(string_array))  # still an array

# However, if we do any mathematical operations, we get a type error
try:
    print(string_array/2)
except TypeError as e:
    print(e, e.__traceback__)

# there's a ton more of things to do with arrays with numpy, but I won't go over it here
