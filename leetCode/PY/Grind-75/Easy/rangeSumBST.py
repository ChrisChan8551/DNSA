# https://leetcode.com/problems/range-sum-of-bst/

# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].


#! Example 1:
# Input: root = [10,5,15,3,7,None,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

#! Example 2:
# Input: root = [10,5,15,3,7,13,18,1,None,6], low = 6, high = 10
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.


# Constraints:

# The number of nodes in the tree is in the range [1, 2 * 104].
# 1 <= Node.val <= 105
# 1 <= low <= high <= 105
# All Node.val are unique.

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rangeSumBST(root, low, high):
    if not root:
        return 0
    stack = [root]
    total = 0
    while stack:
        current = stack.pop()

        if current:
            if low <= current.val <= high:
                total += current.val
            if current.val > low:
                stack.append(current.left)
            if current.val < high:
                stack.append(current.right)
    return total


#! Example 1:
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.right = Node(18)
low = 7
high = 15
print(rangeSumBST(root, low, high))
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

#! Example 2:
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(13)
root.right.right = Node(18)
root.left.left.left = Node(1)
root.left.right.left = Node(6)
low = 6
high = 10
print(rangeSumBST(root, low, high))
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
