"""
decorators are cool because you can add to existing codeblocks, keeping code entirely functional

essentially, you make a parent decorator function that accepts a function as an argument, then a nested function within
that which accepts args, kwargs or named args. These are the arguments that we are passing to the non decorator function
we want to call

for example
"""


def decorate_message(fun):
    # decorators need to encapsulate another function that performs the replacement function
    def add_welcome(
        *args,
    ):  # we can use *args to make a generic decorator or named args for more specific
        return "Welcome to " + fun(*args)

    # Decorator returns a function
    return add_welcome


@decorate_message
def site(site_name):
    return site_name


def site_no_dec(site_name):
    return site_name


print(
    "because the function has a decorator, the decorator function executes the function instead"
)
print(site("StackOverflow"))
print("otherwise it would be")
print(site_no_dec("StackOverflow"))
