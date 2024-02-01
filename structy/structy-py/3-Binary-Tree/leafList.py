# Write a function, leaf_list, that takes in the root of a binary tree and returns a list containing the values of all leaf nodes in left-to-right order.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#! iterative
# def leaf_list(root):
#     # edge case if root is None
#     if root is None:
#         return []
#     # depthfirst
#     stack = [root]
#     leaf = []
#     while stack:
#         node = stack.pop()
#         if node.right is not None:
#             stack.append(node.right)
#         if node.left is not None:
#             stack.append(node.left)
#         # the leaf node has no left and right children then add to leaf list
#         if node.left is None and node.right is None:
#             leaf.append(node.val)
#     return leaf

#! recursion


def leaf_list(root):
    if root is None:
        return []

    if root.left is None and root.right is None:
        return [root.val]
    left = leaf_list(root.left)
    right = leaf_list(root.right)
    return left + right


#!TEST_00
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(leaf_list(a))  # -> [ 'd', 'e', 'f' ]

#!TEST_01
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h

print(leaf_list(a))  # -> [ 'd', 'g', 'h' ]

#!TEST_02
a = Node(5)
b = Node(11)
c = Node(54)
d = Node(20)
e = Node(15)
f = Node(1)
g = Node(3)

a.left = b
a.right = c
b.left = d
b.right = e
e.left = f
e.right = g

#        5
#     /    \
#    11    54
#  /   \
# 20   15
#      / \
#     1  3

print(leaf_list(a))  # -> [ 20, 1, 3, 54 ]

#!TEST_03
x = Node('x')

#      x

print(leaf_list(x))  # -> [ 'x' ]

#!TEST_04
print(leaf_list(None))  # -> [ ]
