# Write a function, depth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in depth-first order.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#!iterative


# def depth_first_values(root):
#     # edge case if root is None return []
#     if root is None:
#         return []
#     # assign variable to track an array of values
#     result = []
#     # assign a stack starting with root value
#     stack = [root]
#     # if stack is not empty then pop the value from stack
#     while len(stack):
#         node = stack.pop()
#         # add the node to the array
#         result.append(node.val)
#         # check if node right is not None
#         if node.right is not None:
#             stack.append(node.right)
#         # check if node left is not None
#         if node.left is not None:
#             stack.append(node.left)
#     # return final result
#     return result

#! recursive
def depth_first_values(root):
    if root is None:
        return []
    left = depth_first_values(root.left)
    right = depth_first_values(root.right)
    return [root.val, *left, *right]


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

print(depth_first_values(a))
#   -> ['a', 'b', 'd', 'e', 'c', 'f']

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

print(depth_first_values(a))
#   -> ['a', 'b', 'd', 'e', 'g', 'c', 'f']

#!TEST_02
a = Node('a')
#     a
print(depth_first_values(a))
#   -> ['a']

#!TEST_03
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
a.right = b
b.left = c
c.right = d
d.right = e

#      a
#       \
#        b
#       /
#      c
#       \
#        d
#         \
#          e

print(depth_first_values(a))
#   -> ['a', 'b', 'c', 'd', 'e']

#!TEST_04
print(depth_first_values(None))
#   -> []
