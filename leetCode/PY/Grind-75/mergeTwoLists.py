# https://leetcode.com/problems/merge-two-sorted-lists/

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.


# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]


# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#! recursive


def mergeTwoLists(list1, list2):
    if (list1 == None):
        return list2
    if (list2 == None):
        return list1
    if (list1.val < list2.val):
        next1 = list1.next
        list1.next = mergeTwoLists(next1, list2)
        return list1
    else:
        next2 = list2.next
        list2.next = mergeTwoLists(list1, next2)
        return list2

#! iterative


def mergeTwoLists(list1, list2):
    dummyHead = ListNode(0)
    tail = dummyHead
    while (list1 and list2):
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
    return dummyHead.next
