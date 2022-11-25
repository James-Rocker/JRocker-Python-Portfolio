# bytearray are very similar to bytes except they are mutable
prime_numbers = [2, 3, 5, 7]

# convert list to bytearray
byte_array = bytearray(prime_numbers)
print(byte_array)

# doing something similar to bytes
list_of_ints = [1, 2, 3, 4]
arr = bytearray(list_of_ints)
print(arr)
arr.append(5)
print(arr)

# but if we try to do the same to bytes
arr = bytes(list_of_ints)
print(arr)
try:
    arr.append(5)
    print(arr)
except AttributeError as e:
    print(e, e.__traceback__)
