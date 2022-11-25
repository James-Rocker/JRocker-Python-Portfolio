import asyncio
import time
from functools import wraps

# timer decorator for async functions


def async_timer_decorator(func):
    # check this a coroutine first
    async def check_coroutine(func, *args, **params):
        if asyncio.iscoroutinefunction(func):
            return await func(*args, **params)  # actually executes the coroutine
        else:
            print("this is not a coroutine")
            return func(
                *args, **params
            )  # executes the sync function anyway, but we warn the user it's unnecessary

    # we use wraps here as it's a decorator for decorators and copies metadata like __name__, __docstring__, __module__
    @wraps(func)
    async def wrapper(*args, **kwargs):  # we still have to pass the args and kwargs
        start_time = time.perf_counter()
        try:
            # because we pass the function with wraps, the *args and **kwargs, we pass this to the
            return await check_coroutine(func, *args, **kwargs)
        finally:
            total_time = time.perf_counter() - start_time  # calculates the time taken
            # prints out the timing once the functions run
            print(f"Function `{func.__name__}` took: {total_time:.4} seconds")

    print(
        "function collected:",
        wrapper.__name__,
        "see here, the wrapper function isn't aware of the args or kwargs values:",
        wrapper.__code__.co_argcount
    )
    return wrapper


# dummy async function, with the wrapper
@async_timer_decorator
async def do_a_thing(each):
    print(each)
    return each


@async_timer_decorator
def do_a_thing_sync(each):
    print(each)
    return each


for number in range(20):
    asyncio.run(do_a_thing(number))

# we can also run this for sync functions although the console is printed out showing its unnecessary
asyncio.run(do_a_thing_sync(5))
