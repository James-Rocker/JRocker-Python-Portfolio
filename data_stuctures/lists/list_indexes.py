from typing import List

my_list: List = []

for each in range(5):
    my_list.append(each)

# [0, 1, 2, 3, 4]
print(my_list)

# 2 because python, arrays start at 0
print(my_list[2])

# 4 get the last item in the list
print(my_list[-1])

# [2, 3, 4] the colon basically says we want the rest of the list
print(my_list[2:])

# [0, 1, 2] the colon before the number says we want everything before
print(my_list[:-2])

for each in range(5):
    my_list.append(f"bleep {each}")

# we can also get the index of an object using
index = my_list.index("bleep 3")
print(index)
