import random


class GiveRandomVal:
    def __init__(self, item):
        self.item = item

    def __getitem__(self, index):
        """
        Get item is the indexer used in class. We are overwriting this for a random item from the list.

        """
        return random.choice(self.item)


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    random_val = GiveRandomVal(my_list)

    print(random_val[0])  # Output: Random element from my_list
    print(random_val[0])  # Output: Another random element from my_list
    print(iter(random_val))