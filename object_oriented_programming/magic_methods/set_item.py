from typing import List


class SetItem:
    def __init__(self, item: List):
        self.item = item

    def __setitem__(self, index, item1):
        """
        Overwrites the default setitem magic method. This is useful in this example for error handling
        """
        try:
            self.item[index] = item1
        except IndexError:
            # because we aren't raising an error, our program can keep running after notifying the error instead of
            # the default behaviour which is raising the index error
            print("The Index you passed does not match the list object provided")


if __name__ == "__main__":
    my_list = [10, 20, 30, 40]
    setter = SetItem(my_list)

    setter[2] = 100  # Replace the item at index 2
    print(my_list)  # Output: [10, 20, 100, 40]

    setter[10] = 200  # Try to replace an item at an invalid index
