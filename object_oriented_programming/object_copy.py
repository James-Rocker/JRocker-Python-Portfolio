import copy

"""
Let's have a look at copying arrays. First let's try making a new reference of the object
"""
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, "a"]
old_list = [a, b, c]
print("Old list value", old_list)
new_list = old_list
new_list[2][2] = 9
print("Modified the new list to correct the value, new value is", new_list)
print(
    "Let's check on the old list:", old_list, "huh that's changed as well as the new "
)
print(
    "Oh. So do the ids match?",
    id(old_list) == id(new_list),
    "how about the value?",
    new_list == old_list,
)

"""
Wack, we need a way to copy something and make a new reference. Let's try the copy module
"""

c = [
    7,
    8,
    "a",
]  # have to redeclare the value because the above, modifies the original object value
print("let's retry that but use the copy module instead")
old_list = [a, b, c]
copied = copy.copy(old_list)
copied[2][2] = 9

print("Using the shallow copy")
print("Modified the new list to correct the value, new value is", copied)
print("Let's check on the old list:", old_list)
print(
    "Let's check ID, is it the same?",
    id(copied) == id(old_list),
    "how about the values?",
    copied == old_list,
)
print(
    "Checking the array object IDs, 1st",
    id(copied[0]) == id(old_list[0]),
    "2nd",
    id(copied[1]) == id(old_list[1]),
)

"""
Okay, so we have copied the object instead of just referencing it. However, the original value is still being modified
when changing the copied object. Why is that? By default, the module makes a shallow copy. However, we have two ways of
copying; shallow copy and deep copy. Shallow copy makes a new object and then inserts references to the old object 

while deep copy recursively copies each object in the original and makes each object new
"""

c = [7, 8, "a"]
old_list = [a, b, c]
deep_copy = copy.deepcopy(old_list)
deep_copy[2][2] = 9

print(
    "Let's check ID, is it the same?",
    id(deep_copy) == id(old_list),
    "how about the values?",
    deep_copy == old_list,
)
print(
    "Checking the array object IDs, 1st",
    id(deep_copy[0]) == id(old_list[0]),
    "2nd",
    id(deep_copy[1]) == id(old_list[1]),
)
