# https://leetcode.com/problems/rotate-list/

# Given the head of a linked list, rotate the list to the right by k places.


# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Example 2:
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]


# Constraints:

# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotateRight(head, k):
    #! edge case if k is larger than linked lis
    #brute force
    #keep moving the last node to the front K times
    # can we find the length of the LL and subtract k?
    #we can reverse the list so that we can have access to the tail (which is now the head)


    if not head:
        return []
    count = 0
    current = head
    while current:
        current = current.next
        count +=1
    print(count)
    pass


#! Example 1:
head = [1, 2, 3, 4, 5]
k = 2
print(rotateRight(head, k))
# Output: [4,5,1,2,3]

#! Example 2:
head = [0, 1, 2]
k = 4
print(rotateRight(head, k))
# Output: [2,0,1]
