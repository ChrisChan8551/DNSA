# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Given the root of a binary tree, flatten the tree into a "linked list":

# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.


# Example 1:


# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [0]
# Output: [0]


# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100

# Hint 1
# If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # pre-order traversal -> DFS - usually means recursive calls
        # process current node, traverse the left, then traverse the right side
        # base case: when node is null
        # takes care of both leaves and nodes that are missing 1 child
        # reassign pointers
        # 1) save right now
        # 2) root.right = root.left
        # 3) left tail.right = temp
        # 4) cleanup = root.left = None
        # 5) find the tail
        # if right_tail exists, it is right
        # elif left_tail exists, it is left
        # else current node
        def _dfs(node):
            if not node:
                return
            left_tail = _dfs(node.left)
            right_tail = _dfs(node.right)



            if node.left:
                temp = node.right
                node.right = node.left
                left_tail.right = temp
                node.left = None

            if right_tail:
                return right_tail
            elif left_tail:
                return left_tail

            else:
                return node

        _dfs(root)


# def flatten(self, root: Optional[TreeNode]) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         current = root
#         while current:
#             if current.left:
#                 temp = current.left
#                 while temp.right:
#                     temp = temp.right
#                 temp.right = current.right
#                 current.right = current.left
#                 current.left = None
#             current = current.right
