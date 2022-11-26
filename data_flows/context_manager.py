import contextlib
import time

"""
context managers are interesting because you can allocate resources when you want.

This is great if we want to open files

we can do this with the dunder or "magic methods" __enter__ and __exit__ and this allows us to use the
`with` statement which implicitly runs these methods on startup and exit

The way I like to think these work is that
__enter__  acts as a try statement
__exit__ acts as the `finally` portion of the same try statement

You might notice, these dunder methods will need to be done in order then to accomplish this, and you'd be right
"""


class DummyClass:
    def __init__(self):
        # initialised attributes, useful for how we want read a file, something like decode methods
        print("__init__")

    def __enter__(self):
        print("__enter__")

    def __exit__(self, exit_type, exit_val, exit_traceback):
        """
        You might notice we are passing 3 exit args. This is done so on error, __exit is raised and this information
        is given to the end user to explain what went wrong

        exit_type = the class exception
        exit_val = the type of exception
        exit_traceback = the traceback, what's needed to resolve
        """
        print("__exit__")

    def __del__(self):
        """
        destructor method and used to delete attributes of a class and unlike delete, operates implicitly
        after the program ends
        """
        print("__del__")


# As you can see from the printout if you run this file, these dunder methods are run in order
with DummyClass():  # both init and enter happen here
    print("body")


class ContextWithMethods:
    def __init__(self):
        print("initializing context")
        self.x = 0

    def __enter__(self):
        print("entering context")
        self.x = 5
        return self

    def add(self, y):
        self.x = self.x + y

    def subtract(self, y):
        self.x = self.x - y

    def __exit__(self, exit_type, exit_val, exit_tb):
        print("\nInside __exit__")
        print("Execution type:", exit_type)
        print("Execution value:", exit_val)
        print("Traceback:", exit_tb)


with ContextWithMethods() as c:
    print("the context manager attribute", c.x)
    c.add(5)
    print(c.x)
    c.add(5)
    print(
        "After calling the method twice, we can see the attribute state is saved", c.x
    )

"""
If you want something cleared up, the best place to do it is in __exit__. One thing that introduces some complexity
is the __del__ method.
 
The __del__ method this mean that memory allocated to the context manager objects doesn't get cleaned up once all
references are complete. Note, __del__ is called when the garbage collector happens to be collecting the objects, not
when you lose the last reference to an object and not when you execute del.

If we want to cleanup the object at an explicit point, it's easier to just del the object
"""

del c

try:
    print(c)
except NameError as e:
    print(e, e.__traceback__)

"""
You might notice these are all class based which is useful but feels like a lot of boiler plating
We can also make context managers with the contextlib builtin library

theres also asynccontextmanager for async functions

This works as a generator where yield raises any errors, then finally does something (acting as the __exit__)
"""


@contextlib.contextmanager
def timer():
    start = time.monotonic()
    try:
        yield time.clock_getres(time.CLOCK_MONOTONIC)
    except BaseException as e:
        print(f"Failed {e}: {time.monotonic() - start}s")
        raise
    finally:
        # if no errors were raised do this
        # thing.close()  # we should also call fileObject close here
        print(f"Total time taken: {time.monotonic() - start}s")


with timer() as c:
    print("we can do a thing here!")
    print("then here")
    print("okay, I'm out, let's get the timing")
