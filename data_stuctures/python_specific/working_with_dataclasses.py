import json
from dataclasses import dataclass

"""
dataclasses are cool because we can make a class and it automatically adds special methods
to the class and exist to store state. Saving us having to write
__init__
__hash__
__eq__
__repr__
__str__
"""


@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 5

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand


fish = InventoryItem("fish", 10)
print("works like a normal class: ", fish.total_cost())
print("as a dict:", fish.__dict__)
print("we haven't implemented an __eq__ method but returns", fish.__eq__(0))
print("the representation of the object", fish.__repr__())
print("as a string", type(fish.__str__()))
print("example of the attributes:", fish.__getattribute__("name"))
print(type(fish))  # as you can see, the type is the class name

"""
one thing to be mindful when making a dataclass is other languages don't recognise custom data types from class so
they need to be converted back into generic objects

Something like the below
"""

print(json.dumps(fish.__dict__))
