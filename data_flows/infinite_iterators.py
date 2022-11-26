import itertools
from time import time

"""
itertools is used to iterate over data structures that can be stepped over using a for loop. These are called iterables

There two types, finite iterators and infinite iterators
infinite: run indefinitely unless the stopping condition is met
finite: terminates
"""

# simple iteration, only doing something every x step until a condition is met
result = itertools.count(start=0, step=2)
for number in result:
    if number < 8:
        print(number)
    else:
        break


# without itertools, we'd be looking at something like this
range_result = range(20)
for range_number in range_result:
    if range_number < 8:
        pass
    else:
        break
    if (range_number % 2) == 0:
        print(range_number)
    else:
        pass


# however, if we want to change the iteration, it's much more work and more importantly, stops after the range
# has been met, not the break value

# cycle. Loops through all the values that are given as an argument to this method sequentially
result = itertools.cycle("12345")
counter = 0
for number in result:
    if counter < 13:
        print(number)
        counter = counter + 1
    else:
        break


# repeat, works really well for zip or maps and looping through x number of times
result = list(map(pow, range(10), itertools.repeat(2)))

for word in result:
    print(word)


def do_a_thing():
    output = 1 + 2
    return output


# You might think, what's the point, you can just use range, have a look at the performance
iter_start_time = time()
for _ in itertools.repeat(None, 10000):
    do_a_thing()
iter_end_time = time()


range_start_time = time()
for _ in range(10000):
    do_a_thing()
range_end_time = time()

# as you can see, iterables are faster in some cases
print("iter time", iter_end_time - iter_start_time)
print("range time", range_end_time - range_start_time)
