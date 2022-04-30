from dataclasses import dataclass
import random
from typing import List


class Distance:
    def __init__(self, x=None, y=None):
        self.ft = x
        self.inch = y

    def __add__(self, x):
        temp = Distance()
        temp.ft = self.ft + x.ft
        temp.inch = self.inch + x.inch
        if temp.inch >= 12:
            temp.ft += 1
            temp.inch -= 12
            return temp

    def __str__(self):
        return f"{self.ft}ft {self.inch}in"


class GiveRandomVal:
    def __init__(self, item):
        self.item = item

    def __getitem__(self, index):
        return random.choice(self.item)


class SetItem:
    """
    Initialise a list and replace an indexed object in the list
    """

    def __init__(self, item: List):
        self.item = item

    def __setitem__(self, index, item1):
        try:
            self.item[index] = item1
        except IndexError:
            print("The Index you passed does not match the list object provided")


@dataclass
class Vector2D:
    x: float = 0
    y: float = 0

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __mul__(self, other):
        return Vector2D(other * self.x, other * self.y)

    def __rmul__(self, other):
        return self * other
