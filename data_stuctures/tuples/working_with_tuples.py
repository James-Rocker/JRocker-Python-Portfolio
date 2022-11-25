from typing import Tuple

# tuples are cool, they are like lists except, they are immutable
my_first_tuple: Tuple = ("hello", "there", "my", "dude")

# we can get objects in the same way as lists
print(my_first_tuple[2])

# python has some neat methods
print(my_first_tuple.count("hello"))  # count occurrences within the tuple
print(my_first_tuple.index("hello"))  # gets the index of the object

# because tuples are immutable, we can't update it with traditional means but there are some workarounds
tuple_as_list = list(my_first_tuple)
tuple_as_list[3] = "man"
my_first_tuple = tuple(tuple_as_list)

print(my_first_tuple)
