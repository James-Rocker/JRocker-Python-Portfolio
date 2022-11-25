from collections import defaultdict

# if you are missing a value in a dict you get a traceback error if you search for it
a_dict = {
    "Terry": "Pokemon",
    "Gabu": "Digimon",
}

try:
    print(a_dict["missing_key"])
except KeyError:
    print("oh dear, the key is missing")
    pass

# you could use get method which provides a default value if it's missing
print(a_dict.get("missing_key", "default value"))

# Instead, we can instead look at the collections library and create a default value entirely
# default_dict is a dict with default factory
int_dict = defaultdict(int, a=10, b=12, c=13)
print(int_dict)
print(int_dict[3])

# we can also use it for default strings
str_dict = defaultdict(str, a="hello", b="world", c="goodbye moon")
print(str_dict)
print(
    str_dict[3]
)  # you'll notice a blank line in the printout, that's because it defaults to a blank string
print(
    "blank value added: ", str_dict
)  # it also adds the value to the dict with a blank value

# we can also do the same for float, lists, dicts, tuples and sets (also the shown ints and str)
# we can also add values with the same update command as dicts or by passing the key, value
str_dict.update(name="John", action="ran")
str_dict["Mary"] = "walked"
print("added value: ", str_dict)


# to change the default value we need to pass it via a function
def test_function():
    return "Default value by usual function"


test_function_dict = defaultdict(test_function)
test_function_dict[1] = "beep"
print("function default value example:", test_function_dict, test_function_dict[0])

# or via lambda
lambda_dict = defaultdict(lambda: "oh, one liner")
lambda_dict[1] = "beep"
print("lambda default value example:", lambda_dict, lambda_dict[0])

# or if you want to update the default value after initialization
str_dict.default_factory = (
    lambda: "I'm not here"
)  # it does still have to be through a lambda or function call
print("update after initialization: ", str_dict["Sam"])

# Like any dict, they are mutable. So, we can update values by just replacing the value
int_dict["a"] = 99
print("int_dict, updated value", int_dict)

# finally, we can also change the default dict object to a dict again
dict_lambda = dict(lambda_dict)
print(
    dict_lambda, dict_lambda[0], "I am a dict?", isinstance(lambda_dict, dict)
)  # but default dict is a dict
