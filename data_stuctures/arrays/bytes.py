import sys

# bytes are immutable byte objects
message = "Python is fun"

# convert string to bytes
byte_message = bytes(message, "utf-8")  # we encode with utf8
print(byte_message, "then converted back to a string:", byte_message.decode("utf-8"))

# we can turn lists, string, objects, and ints.
byte_for_list = [1, 2, 3, 4, 5]

byte_array = bytes(byte_for_list)
print(byte_array, "then back to list of ints", list(byte_array))

# we can also make a byte based on a size
size = 10
arr = bytes(size)
print(arr, "then to lists again", list(arr))

# so why do we use bytes? They seem very similar but inconvenient to work with

a_string = "hello world, I am a thing!"
a_byte_string = bytes(a_string, "utf-8")
print("strings byte size is: ", sys.getsizeof(a_string))
print("byte type byte size is: ", sys.getsizeof(a_byte_string))

"""
so it allows for data to be smaller, but also data needs to be encoded before written and read from disk

bytes consists of sequences of 8-bit unsigned values, while str consists of sequences of Unicode code
"""
