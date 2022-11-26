import statistics
from functools import cache, cached_property, lru_cache
from time import time

"""
caching is cool because we can memorize previously calculated values to save time in the future

python has a couple of ways to do this with lru_cache
"""


@cache
def factorial(n):
    return n * factorial(n - 1) if n else 1


fact_ten_start = time()
factorial(10)  # no previously cached result, makes 11 recursive calls
fact_ten_end = time()
print(fact_ten_end - fact_ten_start)  # takes the longest as it's the initial run

fact_five_start = time()
factorial(5)
fact_fie_end = time()
print(
    fact_fie_end - fact_five_start
)  # as you can see, the results are already cached, so it takes no time at all

fact_twelve_start = time()
factorial(12)
fact_twelve_end = time()
print(
    fact_twelve_end - fact_twelve_start
)  # some or the results are already cached so this is faster than fact_ten


# we can also set cached values for properties
class DataSet:
    def __init__(self):
        self.result = 100

    @property
    def increase(self):
        self.result = self.result + 50
        return self.result

    @cached_property
    def increase_cache(self):
        self.result = self.result + 50
        return self.result


obj = DataSet()
print(
    obj.increase, obj.increase, obj.increase
)  # as you can see, this increases the initialised class attribute
print(
    obj.increase_cache, obj.increase_cache, obj.increase_cache
)  # cached properties, the value is calculated once


# lru stands for last recent used and
@lru_cache(
    maxsize=None
)  # max size will remember the max size results of calls. So 5 remembers the last 5 calls
def fib(n):
    # fib example
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(20))
print(fib(30))
print(fib(40))
print(fib(50))
print(fib.cache_info())  # the benefit of lru_cache is we can get the cache_info
