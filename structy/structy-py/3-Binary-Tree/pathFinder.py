# Write a function, path_finder, that takes in the root of a binary tree and a target value. The function should return an array representing a path to the target value. If the target value is not found in the tree, then return None.

# You may assume that the tree contains unique values.

from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# transverse through the tree until it reaches the target
# assign path as array to keep track of nodes until it reaches last node
# return the paths
# edge cases if root is None
# depth first transversal


def path_finder(root, target):
    # Call the private helper function _path_finder to find the path.
    result = _path_finder(root, target)
    # If the result is None (target not found), return None.
    if result is None:
        return None
    else:
        # If the path is found, reverse it and return the reversed path.
        return result[::-1]

# Private helper function to recursively find the path from the root to the target value.


def _path_finder(root, target):
    # If the current node is None, return None (base case).
    if root is None:
        return None

    # If the current node's value matches the target value, return a list with the current node's value as a single element (path found).
    if root.val == target:
        return [root.val]

    # Recursively search for the target value in the left subtree.
    left_path = _path_finder(root.left, target)
    # If the left_path is not None (target found in the left subtree), append the current node's value and return the path.
    if left_path is not None:
        left_path.append(root.val)
        return left_path

    # If the target value is not found in the left subtree, recursively search in the right subtree.
    right_path = _path_finder(root.right, target)
    # If the right_path is not None (target found in the right subtree), append the current node's value and return the path.
    if right_path is not None:
        right_path.append(root.val)
        return right_path

    # If the target value is not found in either subtree, return None (target not found).
    return None


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

print(path_finder(a, 'e'))  # -> [ 'a', 'b', 'e' ]

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

# print(path_finder(a, 'p'))  # -> None

# #!TEST_02
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

# print(path_finder(a, "c"))  # -> ['a', 'c']

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

# print(path_finder(a, "h"))  # -> ['a', 'c', 'f', 'h']

# #!TEST_04
# x = Node("x")

# #      x

# print(path_finder(x, "x"))  # -> ['x']

# #!TEST_05
# print(path_finder(None, "x"))  # -> None

# #!TEST_06
# root = Node(0)
# curr = root
# for i in range(1, 19500):
#     curr.right = Node(i)
#     curr = curr.right

# #      0
# #       \
# #        1
# #         \
# #          2
# #           \
# #            3
# #             .
# #              .
# #               .
# #              19498
# #                \
# #                19499

# print(path_finder(root, 16281))  # -> [0, 1, 2, 3, ..., 16280, 16281]
