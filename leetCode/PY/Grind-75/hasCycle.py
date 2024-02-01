# https://leetcode.com/problems/linked-list-cycle/

# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# Example 3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.


# Constraints:

# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.


# Follow up: Can you solve it using O(1) (i.e. constant) memory?
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#! also can be used to detect if there are loops within a linked list
#! use slow, fast pointer method to detect connecting nodes in linked list
def hasCycle(head):
    if head == None or head.next == None:  # edge case if there's no nodes
        return False
    slow = fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# Create nodes
node0 = ListNode(3)
node1 = ListNode(2)
node2 = ListNode(0)
node3 = ListNode(-4)

# Connect nodes
node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node1  # Create a cycle

# Set the head of the linked list
head = node0

# Example 2
node0 = ListNode(1)
node1 = ListNode(2)
node0.next = node1
node1.next = node0  # Create a cycle
head_example2 = node0

# Example 3
node0 = ListNode(1)
head_example3 = node0

print(hasCycle(head))
# Output: true
print(hasCycle(head_example2))
# Output: true
print(hasCycle(head_example3))
# Output: false
