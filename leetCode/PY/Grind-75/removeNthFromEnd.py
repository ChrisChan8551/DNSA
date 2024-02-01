# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Given the head of a linked list, remove the nth node from the end of the list and return its head.


# Example 1:

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]

def removeNthFromEnd(head, n):
    slow = fast = head
    # this sets fast point to jump ahead N times so that the slow pointer will stop right before the node that needs to be removed.
    for _ in range(n):
        fast = fast.next

    # edge case if link list is too short
    if not fast:
        return head.next

    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head
