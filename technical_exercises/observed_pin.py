from itertools import product

possible_numbers = {
    '1': ['1', '2', '4'],
    '2': ['1', '2', '3', '5'],
    '3': ['3', '2', '6'],
    '4': ['1', '4', '5', '7'],
    '5': ['2', '4', '5', '6', '8'],
    '6': ['3', '5', '6', '9'],
    '7': ['4', '7', '8'],
    '8': ['0', '5', '7', '8', '9'],
    '9': ['6', '8', '9'],
    '0': ['0', '8']
}


def get_pins(observed):
    list_of_lists = []

    for number in observed:
        list_of_lists.append(possible_numbers[number])

    if len(observed) == 1:
        return list_of_lists[0]
    else:
        unique_items = list(product(*list_of_lists))
        joiner = "".join
        return [joiner(numbers) for numbers in unique_items]


print(get_pins('8'))
print(get_pins('422'))
print(get_pins('4269888'))
