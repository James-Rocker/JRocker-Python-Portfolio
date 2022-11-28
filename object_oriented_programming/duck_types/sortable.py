"""
If we want to make a class sortable in a list of other class instances, python has a few useful ways

__lt__- less than
__gt__ - greater than
__le__ - less than or equal to
__ge__ - greater than or equal to

You need all 4 to accurately sort the objects within a user defined class
This means we can call the sort method on the list of class objects
"""


from functools import total_ordering


class A:
    def __init__(self, score):
        self.score = score

    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score

    def __le__(self, other):
        return self.score <= other.score

    def __ge__(self, other):
        return self.score >= other.score


object_list = [A(10), A(100), A(999)]
object_list.sort()
for each in object_list:
    print(each.score)


class B:
    def __init__(self, score):
        self.score = score

    def __lt__(self, other):
        return self.score < other.score


object_list = [B(10), B(999), B(999), B(100)]
object_list.sort(reverse=True)
for each in object_list:
    print(each.score)

"""
Even if we don't define each individually, they still work.

However, pep8 recommends against it. Instead we should use the lazy method functools.total_ordering()
This builtin, given a class defining one or more rich comparison ordering methods, this class decorator supplies the
rest

For example, we still need to define __eq__ and one rich sorting method e.g. __lt__
"""


@total_ordering
class C:
    def __init__(self, score):
        self.score = score

    def __lt__(self, other):
        return self.score < other.score

    def __eq__(self, other):
        print(other.__dict__)
        return self.score == other.score


object_list = [C(10), C(999), C(999), C(100)]
object_list.sort(reverse=True)
for each in object_list:
    print(each.score)
