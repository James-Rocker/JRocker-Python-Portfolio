from timeit import default_timer as timer

# removing values from a list
int_list = [0] * 10000


# list comprehensions is really fast
def remove_value(sample_list, val):
    return [x for x in sample_list if x != val]


start = timer()
remove_value(int_list, 0)
end = timer()
print(end - start)

int_list = [0] * 10000


# hilariously, if the item is not in the list, this is faster
def remove_value_while(sample_list, val):
    while val in sample_list:
        sample_list.remove(val)
    return int_list


second_start = timer()
remove_value_while(int_list, 0)
second_end = timer()
print(second_end - second_start)
# as you can see, looping methods is important as usually list comprehensions are significantly faster
