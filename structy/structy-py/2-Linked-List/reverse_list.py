# Write a function, reverse_list, that takes in the head of a linked list as an argument. The function should reverse the order of the nodes in the linked list in-place and return the new head of the reversed linked list.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

#! iterative
def reverse_list(head):
    # need to assign 2 pointer strategy. 1 for next, and 1 for prev.
    current = head
    prev = None
    # transverse through the list.
    while current is not None:
        # Assign the NEXT node to another variable, so that current doesn't override current.next
        next = current.next
        # When going to the next node, set current.next to prev before reassigning current to current.next
        current.next = prev
        prev = current
        current = next
    return prev

#! recursive - slightly worse space complexity


# def reverse_list(head, prev=None):  # set default argument of prev to None
#     # base case - return prev if head is None
#     if head is None:
#         return prev
#     # assign next = head.next
#     next = head.next
#     # assign head.next to prev
#     head.next = prev
#     return reverse_list(next, head)


#! TEST_00
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f

print(reverse_list(a))  # f -> e -> d -> c -> b -> a

# #! TEST_01
# x = Node("x")
# y = Node("y")

# x.next = y

# # x -> y

# reverse_list(x) # y -> x

# #! TEST_02
# p = Node("p")

# # p

# reverse_list(p) # p
