def array_diff(a: list, b: list):
    """
    Finds the duplicates in 2 arrays and returns unique values only
    """
    b = set(b)
    return [item for item in a if item not in b]


if __name__ == "__main__":
    print(array_diff([1, 2, 3], [1, 2]))
