# Simple loop through the different objects in the two lists and join together

list1 = ["Good ", "Fair "]
list2 = ["Day", "Sir"]

# List comprehension is really fast and is really fast (see replacing_values.py for example)
res = [x + y for x in list1 for y in list2]
print(res)

# this is the equivalent of
list_obj = []
for each in list1:
    for obj in list2:
        list_obj.append(each + obj)

print(list_obj)

# The list compression is much neater but there are still cases where you might want the longer loops
# logs is the usual reason but if you want multiple things happening then the verbosity can make things clearer
