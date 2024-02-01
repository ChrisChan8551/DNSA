# Write a function, breadth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in breadth-first order.

# use deque from collections to emulate shift()
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#! iterative
def breadth_first_values(root):
    # edge case if root is None return []
    if root is None:
        return []
    # initiate a queue starting with root
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


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

print(breadth_first_values(a))
#    -> ['a', 'b', 'c', 'd', 'e', 'f']

#!TEST_01
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

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

print(breadth_first_values(a))
#   -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

#!TEST_02
a = Node('a')

#      a

print(breadth_first_values(a))
#    -> ['a']

#!TEST_03
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
x = Node('x')

a.right = b
b.left = c
c.left = x
c.right = d
d.right = e

#      a
#       \
#        b
#       /
#      c
#    /  \
#   x    d
#         \
#          e

print(breadth_first_values(a))
#    -> ['a', 'b', 'c', 'x', 'd', 'e']

#!TEST_04
print(breadth_first_values(None))
#    -> []
