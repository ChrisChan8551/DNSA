# Write a function, tree_includes, that takes in the root of a binary tree and a target value. The function should return a boolean indicating whether or not the value is contained in the tree.

# need to import collections deque that imitate .shift() in javascript
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#! breadth
# def tree_includes(root, target):
#     # tranverse through the tree
#     # edge case if root is blank
#     if root is None:
#         return False

#     queue = deque([root])

#     while queue:
#         node = queue.popleft()

#         if node.val == target:
#             return True

#         if node.left:
#             queue.append(node.left)

#         if node.right:
#             queue.append(node.right)

#     return False

#!recursive depth first search


def tree_includes(root, target):
    if root is None:
        return False
    if root.val == target:
        return True
    return tree_includes(root.left, target) or tree_includes(root.right, target)


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

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f

print(tree_includes(a, "e"))  # -> True

# #!TEST_01
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f
# tree_includes(a, "a") # -> True

# #!TEST_02
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f

# tree_includes(a, "n") # -> False

# #!TEST_03
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")
# g = Node("g")
# h = Node("h")

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# f.right = h

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f
# #    /       \
# #   g         h

# tree_includes(a, "f") # -> True

# #!TEST_04
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")
# g = Node("g")
# h = Node("h")

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# f.right = h

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f
# #    /       \
# #   g         h

# tree_includes(a, "p") # -> False

# #! TEST_05
# tree_includes(None, "b") # -> False
