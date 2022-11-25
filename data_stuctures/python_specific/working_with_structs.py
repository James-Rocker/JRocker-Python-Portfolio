import struct

"""
structs are for converting python data types into bytes, allowing us to parse binary files in c in python

It's also great if we know the shape of the object and want to reduce the objects to as small as possible
"""

# 'i 4s f' is integer, 4 characters, float
formatting = "i 4s f"
packed = struct.pack(formatting, 10, b"John", 2500)
# to the pack the items into binary files
print(packed)

# then to unpack
print(
    struct.unpack(formatting, packed)
)  # python always returns the unpacked values as tuples

# let's get the size!
size = struct.calcsize(formatting)
print("Size in bytes: {}".format(size))
print(
    "lets compare against an unstructured size",
    struct.unpack(formatting, packed).__sizeof__(),
)

# as you can see, it's about 4 times smaller
