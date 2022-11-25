from typing import Set

# sets are similar to lists. Sets aren't ordered and need to be entirely unique
my_first_set: Set = {"hello", "world", "goodbye", "moon"}

# honestly, in my career I have never used sets except for removing duplicates
repeat_list = [1, 1, 1, 2, 3, 3, 3, 4]
print(set(repeat_list))

# sets are cool because they actual values are immutable but values can be added and removed
my_first_set.add('bleep')
my_first_set.remove('hello')
print(my_first_set)
