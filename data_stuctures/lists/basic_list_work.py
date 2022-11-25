from typing import List

my_first_list: List = []

# lists in python are mutable. We can add and remove
for each in range(5):
    my_first_list.append(each)

# [0, 1, 2, 3, 4]
print(my_first_list)

# We can also remove
my_first_list.remove(2)

# [0, 1, 3, 4]
print(my_first_list)
