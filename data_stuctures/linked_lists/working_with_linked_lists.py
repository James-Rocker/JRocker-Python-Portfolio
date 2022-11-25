"""
a linked list is sequential data connected by links
each element is contains a connection to another data element in form of a pointer.
Pointers are kinda foreign to Python so does not have linked lists in its standard library

we can try and recreate the functionality here
"""


class Node:
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize with next as null


class LinkedList:
    def __init__(self):
        self.head = None  # any attribute will do nice


linked = LinkedList()
linked.head = Node(1)
second = Node(2)
third = Node(3)

linked.head.next = second
second.next = third


print("so here we can see the next attribute links to the next class obj", second.next, second.data, third.data)

print("we can then show this in practice by chaining the next method and data")
print(linked.head.data)
print(linked.head.next.data)
print(linked.head.next.next.data)
