# Write a function, tree_value_count, that takes in the root of a binary tree and a target value. The function should return the number of times that the target occurs in the tree.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# def tree_value_count(root, target):
#     count = 0
#     stack = [root]
#     if root is None:
#         return 0
#     while stack:
#         node = stack.pop()
#         if node.val == target:
#             count += 1
#         if node.left:
#             stack.append(node.left)
#         if node.right:
#             stack.append(node.right)
#     return count

#! recursion


def tree_value_count(root, target):
    if root is None:
        return 0
    count = 1 if root.val == target else 0
    left = tree_value_count(root.left, target)
    right = tree_value_count(root.right, target)
    return count + left + right


#!TEST_00
a = Node(12)
b = Node(6)
c = Node(6)
d = Node(4)
e = Node(6)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      12
#    /   \
#   6     6
#  / \     \
# 4   6     12

print(tree_value_count(a,  6))  # -> 3


#!TEST_01
a = Node(12)
b = Node(6)
c = Node(6)
d = Node(4)
e = Node(6)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      12
#    /   \
#   6     6
#  / \     \
# 4  6     12

print(tree_value_count(a,  12))  # -> 2

#!TEST_02
a = Node(7)
b = Node(5)
c = Node(1)
d = Node(1)
e = Node(8)
f = Node(7)
g = Node(1)
h = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      7
#    /   \
#   5     1
#  / \     \
# 1   8     7
#    /       \
#   1         1

print(tree_value_count(a, 1))  # -> 4

#!TEST_03
a = Node(7)
b = Node(5)
c = Node(1)
d = Node(1)
e = Node(8)
f = Node(7)
g = Node(1)
h = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      7
#    /   \
#   5     1
#  / \     \
# 1   8     7
#    /       \
#   1         1

print(tree_value_count(a, 9))  # -> 0

#!TEST_04
print(tree_value_count(None, 42))  # -> 0
