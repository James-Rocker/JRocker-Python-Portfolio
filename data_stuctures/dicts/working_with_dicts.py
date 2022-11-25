from typing import Dict

# dicts are cool, they are mutable key, value pairs, and we can also
my_first_dict: Dict = {}
my_first_dict["hey"] = "there"

print(my_first_dict)

second_dict = {
        "Terry": "Pokemon",
        "Gabu": "Digimon",
    }

# python has some built-in methods for getting the objects
print(second_dict.keys())
print(second_dict.values())
print(second_dict.items())  # makes a loopable list for the key, values

# update is a bit of a misnomer because you can easily update values, remove and add keys but adds two dicts together
second_dict.update(my_first_dict)
print("updated dict:", second_dict)

# there's some cool builtins that python offers
# usually del deletes at an index point while pop
del second_dict['Terry']  # removes key-value pair of 'Terry'
my_first_dict.pop('hey')  # we can also remove keys with pop, and we can return the value
# there's also remove() which removes the first occurrence

print("before popping the most recent insert:", second_dict)
second_dict.popitem()  # removes the last inserted item
print("terry has been deleted", second_dict)
