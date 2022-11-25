# frozensets are similar to sets except they are immutable

vowels = ('a', 'e', 'i', 'o', 'u')
created_frozen_set = frozenset(vowels)
print('The frozen set is:', created_frozen_set)
print('The empty frozen set is:', frozenset())

# what happens when passing
mutable_frozen_set = frozenset([1, 1, 1, 2, 3, 3, 3, 4])
print(mutable_frozen_set)  # turns it into a set

# there are some useful benefits of using frozen sets including
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

# copying a frozenset
F = A.copy()  # copy
print("copy", F)
print("union by merging two frozenset together", A.union(B))  # union
print("intersection showing the which values are in both", A.intersection(B))  # intersection
print("difference shows the difference between two", A.difference(B))  # difference
print("symmetrical difference showing positional differences", A.symmetric_difference(B))  # symmetric_difference
