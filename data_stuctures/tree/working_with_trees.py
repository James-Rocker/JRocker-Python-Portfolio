from anytree import Node, RenderTree

# python doesn't do trees, the closet would be to make class and attributes. Instead, lets use anytree

fred = Node("Fred")  # top of the tree
sid = Node("Sid", parent=fred)
liam = Node("Liam", parent=sid)

dan = Node("Dan", parent=fred)
jet = Node("Jet", parent=dan)
jodie = Node("Jodie", parent=dan)
joe = Node("Joe", parent=dan)


for pre, fill, node in RenderTree(fred):
    print("%s%s" % (pre, node.name))


print(dan.children)
