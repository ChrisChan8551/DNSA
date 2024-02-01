# Write a function, create_linked_list, that takes in a list of values as an argument. The function should create a linked list containing each item of the list as the values of the nodes. The function should return the head of the linked list.
#
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

#! Check answer
def create_linked_list(values):
    # first will need to start off creating a new head node
    head = Node(None)
    # return None if there are no values
    # will need to assign a tail for the following nodes / values
    tail = head
    # transverse through the length of the values list and assign to the linked list
    for i in range(len(values)):
        # tail.next should be assigned to the new values
        tail.next = Node(values[i])
        # assign tail to next
        tail = tail.next
    # return the head of the linked list at the end
    return head.next


#! TEST_00
create_linked_list(["h", "e", "y"])
# h -> e -> y

#! TEST_01
create_linked_list([1, 7, 1, 8])
# 1 -> 7 -> 1 -> 8

#! TEST_02
create_linked_list(["a"])
# a

#! TEST_03
create_linked_list([])
# null
