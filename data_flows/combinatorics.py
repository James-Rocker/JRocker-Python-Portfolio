from itertools import permutations, combinations, product, combinations_with_replacement

# product. Find the all combinations of product from a number of iterators
arr1 = [1, 2, 3]
arr2 = [5, 6, 7]
print(list(product(arr1, arr2)))

# combinations. gets a list of all unique possible combinations up to nth length tuples
combo = [1, 2, 3, 4]
print(list(combinations(combo, 2)))

# permutations. Get all permutations of the iterator
perm = permutations([1, 2, 3, 4])
for i in list(perm):
    print(i)

# combination with replacements. Similar to combinations but allows elements to be selected more than once
string_vals = "Hello world"
combo_with_replace = list(combinations_with_replacement(string_vals, 2))
print(
    "similar to the combinations with, get the combinations to r level",
    combo_with_replace,
)
print(string_vals)
