# Write a function, all_tree_paths, that takes in the root of a binary tree. The function should return a 2-Dimensional list where each subarray represents a root-to-leaf path in the tree.

# The order within an individual path must start at the root and end at the leaf, but the relative order among paths in the outer list does not matter.

# You may assume that the input tree is non-empty.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def all_tree_paths(root):
    # depth first transversal recursive since the paths are top down
    # keep an subarrays to keep track of 'paths'
    paths = []
    if root is None:
        return []
    # base case for a 'leaf node'
    if root.left is None and root.right is None:
        return [[root.val]]
    left = all_tree_paths(root.left)
    right = all_tree_paths(root.right)
    for subpath in left:
        paths.append([root.val, *subpath])
    for subpath in right:
        paths.append([root.val, *subpath])
    return paths


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

print(all_tree_paths(a))  # ->
# [
#   [ 'a', 'b', 'd' ],
#   [ 'a', 'b', 'e' ],
#   [ 'a', 'c', 'f' ]
# ]

# #!TEST_01
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
# g = Node('g')
# h = Node('h')
# i = Node('i')

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# e.right = h
# f.left = i

# #         a
# #      /    \
# #     b      c
# #   /  \      \
# #  d    e      f
# #      / \    /
# #     g  h   i

# print(all_tree_paths(a)) # ->
# # [
# #   [ 'a', 'b', 'd' ],
# #   [ 'a', 'b', 'e', 'g' ],
# #   [ 'a', 'b', 'e', 'h' ],
# #   [ 'a', 'c', 'f', 'i' ]
# # ]

# #!TEST_02
# q = Node('q')
# r = Node('r')
# s = Node('s')
# t = Node('t')
# u = Node('u')
# v = Node('v')

# q.left = r
# q.right = s
# r.right = t
# t.left = u
# u.right = v

# #      q
# #    /   \
# #   r     s
# #    \
# #     t
# #    /
# #   u
# #  /
# # v

# print(all_tree_paths(a)) # ->
# # [
# #   [ 'q', 'r', 't', 'u', 'v' ],
# #   [ 'q', 's' ]
# # ]

# #!TEST_03
# z = Node('z')

# #      z

# print(all_tree_paths(a)) # ->
# # [
# #   ['z']
# # ]
