# https://leetcode.com/problems/print-binary-tree/

# Given the root of a binary tree, construct a 0-indexed m x n string matrix res that represents a formatted layout of the tree. The formatted layout matrix should be constructed using the following rules:

# The height of the tree is height and the number of rows m should be equal to height + 1.
# The number of columns n should be equal to 2 ^ (height+1) - 1.
# Place the root node in the middle of the top row (more formally, at location res[0][(n-1)/2]).
# For each node that has been placed in the matrix at position res[r][c], place its left child at res[r+1][c-2height-r-1] and its right child at res[r+1][c+2height-r-1].
# Continue this process until all the nodes in the tree have been placed.
# Any empty cells should contain the empty string "".
# Return the constructed matrix res.


# Example 1:
# Input: root = [1,2]
# Output:
# [["","1",""],
#  ["2","",""]]

# Example 2:
# Input: root = [1,2,3,null,4]
# Output:
# [["","","","1","","",""],
#  ["","2","","","","3",""],
#  ["","","4","","","",""]]


# Constraints:

# The number of nodes in the tree is in the range [1, 210].
# -99 <= Node.val <= 99
# The depth of the tree will be in the range [1, 10].

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def printTree(root):
    # find the width and the depth of the binary tree
    # this help us figure out how big of a matrix to create
    # if we find the depth, we know how many rows we need
    # we can derive the number of columns from the depth
    # prebuild the matrix using the above formula for height and rows
    # nodes can be placed by calculating columns c +/- 2^(height-r-1)
    # fill out matrix values layer by layer with BFS
    # keep track of node, layers (r value), (c value)
    # rows = height + 1
    # columns = 2 ^ (height+1) - 1
    def _get_depth(node, level=0):
        if not node:
            return level
        return max(_get_depth(node.left, level + 1), _get_depth(node.right, level + 1))

    ROWS = _get_depth(COLS)
    COLS = 2**(ROWS) - 1

    res = [[""] * COLS for _ in range(ROWS)]
    queue = deque()
    # (node, layer / row, col)
    queue.append((root, 0, (COLS - 1) // 2))
    while queue:
        node, row, col = queue.popleft()
        res[row][col] = str(node.val)
        if node.left:
            queue.append((node.left, row + 1, col - 2 ** (ROWS - row - 2)))
        if node.right:
            queue.append((node.right, row + 1, col + 2 ** (ROWS - row - 2)))
    return res
