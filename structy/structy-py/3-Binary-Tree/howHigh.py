# Write a function, how_high, that takes in the root of a binary tree. The function should return a number representing the height of the tree.
# The height of a binary tree is defined as the maximal number of edges from the root node to any leaf node.
# If the tree is empty, return -1.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#! iterative
# def how_high(node):
#     # if root is empty return -1
#     if node is None:
#         return -1
#     max_height = -1
#     stack = [(node, 0)]
#     while stack:
#         current, height = stack.pop()
#         if height > max_height:
#             max_height = height
#         if current.right:
#             stack.append((current.right, height+1))
#         if current.left:
#             stack.append((current.left, height+1))
#     return max_height

#! recursive


def how_high(node):
    if node is None:
        return -1
    left_height = how_high(node.left)
    right_height = how_high(node.right)
    return 1 + max(left_height, right_height)


#!TEST_00
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

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

print(how_high(a))  # -> 2

#!TEST_01
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /
#   g

print(how_high(a))  # -> 3

#!TEST_02
a = Node('a')
c = Node('c')

a.right = c

#      a
#       \
#        c

print(how_high(a))  # -> 1

#!TEST_03
a = Node('a')

#      a

print(how_high(a))  # -> 0

#!TEST_04
print(how_high(None))  # -> -1
