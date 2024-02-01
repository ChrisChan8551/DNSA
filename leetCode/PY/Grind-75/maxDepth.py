# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2


# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100

#! iterative
def maxDepth(root):
    if root is None:
        return 0
    max_height = 1
    stack = [(root, 1)]
    while stack:
        current, height = stack.pop()
        if height > max_height:
            max_height = height
        if current.right:
            stack.append((current.right, height+1))
        if current.left:
            stack.append((current.left, height+1))
    return max_height

#! recursive


def maxDepth(root):
    if root is None:
        return 0
    left_height = maxDepth(root.left)
    right_height = maxDepth(root.right)
    return 1 + max(left_height, right_height)
