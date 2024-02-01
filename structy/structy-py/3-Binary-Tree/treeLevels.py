# Write a function, tree_levels, that takes in the root of a binary tree. The function should return a 2-Dimensional list where each sublist represents a level of the tree.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#! iterative


def tree_levels(root):
    if root is None:
        return []
    stack = [(root, 0)]  # adding a tuple or tracking of a level
    levels = []
    while stack:
        node, level_num = stack.pop()  # destructure the stack because now there's 2 elements
        if len(levels) == level_num:  # this checks which level and creates a subarray
            levels.append([node.val])
        else:
            # if level exsists then append node value to the level array
            levels[level_num].append(node.val)
        if node.right:
            stack.append((node.right, level_num+1))
        if node.left:
            stack.append((node.left, level_num+1))
    return levels

#! recursion
# def tree_levels(root):
#     if root is None:
#         return []


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

print(tree_levels(a))  # ->
# [
#   ['a'],
#   ['b', 'c'],
#   ['d', 'e', 'f']
# ]

#!TEST_01
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
i = Node('i')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h
f.left = i

#         a
#      /    \
#     b      c
#   /  \      \
#  d    e      f
#      / \    /
#     g  h   i

print(tree_levels(a))  # ->
# [
#   ['a'],
#   ['b', 'c'],
#   ['d', 'e', 'f'],
#   ['g', 'h', 'i']
# ]

#!TEST_02
q = Node('q')
r = Node('r')
s = Node('s')
t = Node('t')
u = Node('u')
v = Node('v')

q.left = r
q.right = s
r.right = t
t.left = u
u.right = v

#      q
#    /   \
#   r     s
#    \
#     t
#    /
#   u
#  /
# v

print(tree_levels(q))  # ->
# [
#   ['q'],
#   ['r', 's'],
#   ['t'],
#   ['u'],
#   ['v']
# ]

#!TEST_03
print(tree_levels(None))  # -> []
