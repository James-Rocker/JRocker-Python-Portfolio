
def unique_in_order(iterable):
    unique_list = []
    previous = 0
    for each in iterable:
        if len(unique_list) == 0:
            unique_list.append(each)
        elif each != unique_list[previous]:
            unique_list.append(each)
            previous += 1
    return unique_list


print(unique_in_order('AAAABBBCCDAABBB'))
