# https://leetcode.com/problems/add-one-row-to-tree/

# Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.

# Note that the root node is at depth 1.

# The adding rule is:

# Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
# cur's original left subtree should be the left subtree of the new left subtree root.
# cur's original right subtree should be the right subtree of the new right subtree root.
# If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.


#! Example 1:
# Input: root = [4,2,6,3,1,5], val = 1, depth = 2
# Output: [4,1,1,2,null,null,6,3,1,5]

#! Example 2:
# Input: root = [4,2,null,3,1], val = 1, depth = 3
# Output: [4,2,null,1,1,3,null,null,1]


# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# The depth of the tree is in the range [1, 104].
# -100 <= Node.val <= 100
# -105 <= val <= 105
# 1 <= depth <= the depth of tree + 1
from collections import deque


class TreeNode(object):
    def __init__(self, val`=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def addOneRow(root, val, depth):
    """
    :type root: TreeNode
    :type val: int
    :type depth: int
    :rtype: TreeNode
    """
    # BFS needing to find the appropriate depth
    # add these new nodes to the entire row of this depth
    # once we get to depth -1 (last row), create new nodes with the value of val
    # new nodes will have left and right of the original left and right nodes
    # current node's left and right will be updated to the new nodes
    # edge case: depth = 1
    # node (node, layer)
    if depth == 1:
        return TreeNode(val,root,None)
    queue = deque([(root, 1)])

    while queue:
        node, layer = queue.popleft()

        if layer == depth - 1:
            new_left = TreeNode(val, node.left, None)
            new_right = TreeNode(val, None, node.right)

            node.left = new_left
            node.right = new_right

            continue
        if node.left:
            queue.append((node.left, layer + 1))
        if node.right:
            queue.append((node.right, layer + 1))

    return root

#! Example 1:
root = [4, 2, 6, 3, 1, 5]
val = 1
depth = 2
print(addOneRow(root, val, depth))
# Output: [4,1,1,2,null,null,6,3,1,5]

#! Example 2:
root = [4, 2, None, 3, 1]
val = 1
depth = 3
print(addOneRow(root, val, depth))
# Output: [4,2,null,1,1,3,null,null,1]
