# https://leetcode.com/problems/longest-univalue-path/

# Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

# The length of the path between two nodes is represented by the number of edges between them.

#! Example 1:
# Input: root = [5,4,5,1,1,null,5]
# Output: 2
# Explanation: The shown image shows that the longest path of the same value (i.e. 5).

#! Example 2:
# Input: root = [1,4,5,4,4,null,5]
# Output: 2
# Explanation: The shown image shows that the longest path of the same value (i.e. 4).


# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# -1000 <= Node.val <= 1000
# The depth of the tree will not exceed 1000.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def longestUnivaluePath(root):
    # DFS to transverse the entire tree (recursion)
    # check if parent has the same val as the children
    # base case - check if node is null
    # when node is null, then return 0 for no path
    # find max of left and right node when DFS is going back up the tree.

    longest = 0
    #! need a longest variable to keep track of longest path because there are instances where the longest path is in the middle of the tree.
    # if child does not equal the current node, do not take it's return value

    def _dfs(node):
        if not node:
            return 0

        left =_dfs(node.left)
        right = _dfs(node.right)
        left_path = left if node.left and node.val == node.left.val else 0
        right_path = right if node.right and node.val == node.right.val else 0

        path_length = left_path + right_path
        nonlocal longest #function of python to access an out of scope variable
        longest = max(longest, path_length)
        return max(left_path , right_path ) + 1
    _dfs(root)
    return longest


#! Example 1:
root = [5, 4, 5, 1, 1, None, 5]
print(longestUnivaluePath(root))
# Output: 2
# Explanation: The shown image shows that the longest path of the same value (i.e. 5).

#! Example 2:
root = [1, 4, 5, 4, 4, None, 5]
print(longestUnivaluePath(root))
# Output: 2
# Explanation: The shown image shows that the longest path of the same value (i.e. 4).
