# https://leetcode.com/problems/add-two-numbers/

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


#! Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

#! Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

#! Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

# def addTwoNumbers(l1, l2):
#     dummyHead = ListNode()
#     result = dummyHead

#     total = carry = 0

#     while l1 or l2 or carry:
#         total = carry

#         if l1:
#             total += l1.val
#             l1 = l1.next
#         if l2:
#             total += l2.val
#             l2 = l2.next

#         num = total % 10
#         carry = total // 10
#         dummyHead.next = ListNode(num)
#         dummyHead = dummyHead.next

#     return result.next


def addTwoNumbers(l1, l2):
    # create new linked list
    # loop though both linked list
    # if sum is >= 10, add % 10 to next sum
    # use the short list first, and then add the remainder of the longer list to the end.
    dummy_head = ListNode()
    prev = dummy_head 
    carry = 0
    while l1 or l2:
        #create a dummy head for to start the new linked list
        l1_val = 0 if not l1 else l1.val
        l2_val = 0 if not l2 else l2.val

        total = l1_val + l2_val + carry
        current_node = ListNode(total % 10)
        prev.next = current_node
        prev = prev.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
        carry = total // 10


    if carry:
        prev.next = ListNode(carry)

    return dummy_head.next



#! Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

#! Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

#! Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
