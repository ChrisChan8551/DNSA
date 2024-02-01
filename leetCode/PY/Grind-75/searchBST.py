# https://leetcode.com/problems/search-in-a-binary-search-tree/

# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.


# Example 1:
# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]

# Example 2:
# Input: root = [4,2,7,1,3], val = 5
# Output: []


# Constraints:
# The number of nodes in the tree is in the range [1, 5000].
# 1 <= Node.val <= 107
# root is a binary search tree.
# 1 <= val <= 107

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#! recursive
def searchBST(root, val):
    if not root or root.val == val:
        return root
    if val < root.val:
        return searchBST(root.left, val)
    else:
        return searchBST(root.right, val)

# #! iterative
# def searchBST(root, val):
#     while root and root.val != val:
#         if val < root.val:
#             root = root.left
#         else:
#             root = root.right
#     return root

# Example 1:
# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]

# Example 2:
# Input: root = [4,2,7,1,3], val = 5
# Output: []


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

result = searchBST(root, 2)
print(result.val)  # Output: 2
print(result.left.val)  # Output: 1
print(result.right.val)  # Output: 3

result = searchBST(root, 5)
print(result)  # Output: None
