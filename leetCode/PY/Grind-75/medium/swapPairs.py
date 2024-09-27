# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)


# Constraints:
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100


from typing import Optional

# Definition for singly-linked list.class ListNode:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # swap every adjacent pair of nodes
        # list can be empty
        # cannot modify values of list
        # 1) traverse through linked list using while loop.
        # 2) need to create dummy head for new linked list
        # 3) need a fast / slow pointer
        dummy = ListNode(0, head)
        previous = dummy
        current = head

        while current and current.next:
            next_pair = current.next.next
            second = current.next

            # Swap the nodes
            second.next = current
            current.next = next_pair
            previous.next = second

            # Move pointers
            previous = current
            current = next_pair

        return dummy.next

# Helper functions for testing

# Convert list to linked list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Convert linked list to list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test the solution
if __name__ == "__main__":
    sol = Solution()

    # Example 1: [1, 2, 3, 4] -> [2, 1, 4, 3]
    ll = create_linked_list([1, 2, 3, 4])
    swapped = sol.swapPairs(ll)
    print(linked_list_to_list(swapped))  # Output: [2, 1, 4, 3]

    # Example 2: [] -> []
    ll = create_linked_list([])
    swapped = sol.swapPairs(ll)
    print(linked_list_to_list(swapped))  # Output: []

    # Example 3: [1] -> [1]
    ll = create_linked_list([1])
    swapped = sol.swapPairs(ll)
    print(linked_list_to_list(swapped))  # Output: [1]

    # Example 4: [1, 2, 3] -> [2, 1, 3]
    ll = create_linked_list([1, 2, 3])
    swapped = sol.swapPairs(ll)
    print(linked_list_to_list(swapped))  # Output: [2, 1, 3]
