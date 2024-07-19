# https://leetcode.com/problems/create-binary-tree-from-descriptions/

# You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

# If isLefti == 1, then childi is the left child of parenti.
# If isLefti == 0, then childi is the right child of parenti.
# Construct the binary tree described by descriptions and return its root.

# The test cases will be generated such that the binary tree is valid.

#! Example 1:
# Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
# Output: [50,20,80,15,17,19]
# Explanation: The root node is the node with value 50 since it has no parent.
# The resulting binary tree is shown in the diagram.

#! Example 2:
# Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
# Output: [1,2,null,null,3,4]
# Explanation: The root node is the node with value 1 since it has no parent.
# The resulting binary tree is shown in the diagram.


# Constraints:

# 1 <= descriptions.length <= 104
# descriptions[i].length == 3
# 1 <= parenti, childi <= 105
# 0 <= isLefti <= 1
# The binary tree described by descriptions is valid.

#! Hint 1
# Could you represent and store the descriptions more efficiently?
#! Hint 2
# Could you find the root node?
#! Hint 3
# The node that is not a child in any of the descriptions is the root node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def createBinaryTree(descriptions):
    # under constraints there is a minimum length of 1, so that indicates there will be more than 1 edge case
    # hash map to keep access of all created nodes that we will connect
    # return the node without parent
    # iterate through the descriptions, make connections as we go

    hash_map = {}
    parents = set()
    for parent, child, is_left in descriptions:
        if parent not in hash_map:
            hash_map[parent] = TreeNode(parent)
            parents.add(parent)

        node = hash_map[parent]
        child_node = hash_map[child] if child in hash_map else TreeNode(child)
        hash_map[child] = child_node
        parents.discard(child)

        if is_left:
            node.left = child_node
        else:
            node.right = child_node

    root = parents.pop()
    return hash_map[root]


#! Example 1:
descriptions = [[20, 15, 1], [20, 17, 0],
                [50, 20, 1], [50, 80, 0], [80, 19, 1]]
print(createBinaryTree(descriptions))
# Output: [50,20,80,15,17,19]
# Explanation: The root node is the node with value 50 since it has no parent.
# The resulting binary tree is shown in the diagram.

#! Example 2:
descriptions = [[1, 2, 1], [2, 3, 0], [3, 4, 1]]
print(createBinaryTree(descriptions))
# Output: [1,2,null,null,3,4]
# Explanation: The root node is the node with value 1 since it has no parent.
# The resulting binary tree is shown in the diagram.
