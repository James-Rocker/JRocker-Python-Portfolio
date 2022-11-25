import itertools
import operator

list_one = ["a", "b", "c"]
thing = "hello"
set_thing = {"bleep", "bloop"}
iter_four = ["9", "5", "0"]

# takes multiple iterables and goes through each element in each object, one by one
result = itertools.chain(list_one, iter_four, thing, set_thing)
for element in result:
    print(element)

# Compress joins two iterators together and returns corresponding objects that are true
names = ["Alice", "James", "Matt"]
have_flu = [True, True, False]

result = itertools.compress(names, have_flu)
for element in result:
    print(element)


# dropwhile. Applies a function first then returns the rest of the iterator once that returns false once
def is_positive(n):
    print(n)
    return n > 0


value_list = [5, 6, -8, -4, 2]
result = list(itertools.dropwhile(is_positive, value_list))
print(result)

# accumulate, accumulates strings from the iterator
string_numbers = ["1", "2", "3", "4"]

# Iterating List
for each in itertools.accumulate(string_numbers):
    print(each)

# you can also perform an action with an operator for each object in the iterator
numbers = [10, 20, 30, 40]
for each in itertools.accumulate(numbers, operator.add):
    print(each)

# takewhile, does the opposite of dropwhile, only return objects until false then ignore the rest
result = list(itertools.takewhile(is_positive, value_list))
print(result)
