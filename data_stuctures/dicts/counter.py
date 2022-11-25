from collections import Counter

# counters are cool! We can pass a list of objects and counter turns it into a k,v with the frequency as the value
# Counters are a class
list_of_things = [1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 1, 1, 1, 1]
counted = Counter(list_of_things)
print(counted)

# we can also do this with a tuple
tuple_of_things = (1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 1, 1, 1, 1)
print(Counter(tuple_of_things))  # something you may notice is that the count gets sorted in descending order

# or even a string and count the frequency of characters
print(Counter("hello, world. How are you doing?"))

# we can also provide the value with key word arguments or dicts
print(Counter(x=1, y=2, z=3))
dict_counter = Counter({'a': 1, 'b': 2, 'c': 3})
print(dict_counter)

# values can be added to a collection object, and they will be counter
dict_counter.update("x")
print(dict_counter)

# as counters are dicts, we can get the values, change values etc. in the same way we work with dicts
print("Am i a dict?", isinstance(dict_counter, dict), dict_counter["x"], 'with default value of', dict_counter["z"])

# but because it's a class there are some useful methods built in that we can apply
print("the total count of objects", dict_counter.total())
print("the most common objects by x, in this case the 2 most common", dict_counter.most_common(2))
print("get the objects back in the form of a sorted list", sorted(counted.elements()))
