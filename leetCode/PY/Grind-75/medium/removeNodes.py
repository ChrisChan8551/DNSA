# https://leetcode.com/problems/remove-nodes-from-linked-list/

# You are given the head of a linked list.

# Remove every node which has a node with a greater value anywhere to the right side of it.

# Return the head of the modified linked list.


#! Example 1:
# Input: head = [5,2,13,3,8]
# Output: [13,8]
# Explanation: The nodes that should be removed are 5, 2 and 3.
# - Node 13 is to the right of node 5.
# - Node 13 is to the right of node 2.
# - Node 8 is to the right of node 3.

#! Example 2:
# Input: head = [1,1,1,1]
# Output: [1,1,1,1]
# Explanation: Every node has value 1, so no nodes are removed.


# Constraints:

# The number of the nodes in the given list is in the range [1, 105].
# 1 <= Node.val <= 105

# Hint 1
# Iterate on nodes in reversed order.
# Hint 2
# When iterating in reversed order, save the maximum value that was passed before.

# Definition for singly-linked list.
class head:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#! stack solution
def removeNodes(head):
    # check if the next node is greater than current node
    # reverse list, iterate through
    # track largest number seen so far
    # use a stack to backtrack numbers. Top of the stack is the previous node
    # if current < prev node
    # keep popping stack until if current is greater than top of the stack.
    stack = []
    current = head
    while current:
        # checks stack if empty and checks if current value is greater than the top of the stack.
        while stack and current.val > stack[-1].val:
            stack.pop()
        # else add to the stack and move to the next node.
        stack.append(current)
        current = current.next

    # create a new Node by declaring a dummy head
    dummy = head()
    dummyCurrent = dummy
    for node in stack:
        dummyCurrent.next = node
        dummyCurrent = dummyCurrent.next
    return dummy.next


#! recursion
# def removeNodes(head):
#     if not head:
#         return None

#     head.next = removeNodes(head.next)

#     if head.next and head.val < head.next.val:
#         return head.next

#     return head

#! Example 1:
# Input: head = [5,2,13,3,8]
# Output: [13,8]
# Explanation: The nodes that should be removed are 5, 2 and 3.
# - Node 13 is to the right of node 5.
# - Node 13 is to the right of node 2.
# - Node 8 is to the right of node 3.

#! Example 2:
# Input: head = [1,1,1,1]
# Output: [1,1,1,1]
# Explanation: Every node has value 1, so no nodes are removed.
