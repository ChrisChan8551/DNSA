# Write a function, linked_list_values, that takes in the head of a linked list as an argument. The function should return a list containing all values of the nodes in the linked list.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


#! iterative
# def linked_list_values(head):
#     current = head
#     # assign result array
#     stack = []
#     # traverse though the linked list either breadth-first or depth-first
#     while (current != None):
#         stack.append(current.val)
#         current = current.next
#     return stack

#! recursion
def linked_list_values(head):
    if head is None:
        return []
    else:
        return [head.val] + linked_list_values(head.next)


# #! TEST_00
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")

# a.next = b
# b.next = c
# c.next = d

# # a -> b -> c -> d

# linked_list_values(a) # -> [ 'a', 'b', 'c', 'd' ]

# #! TEST_01
# x = Node("x")
# y = Node("y")

# x.next = y

# # x -> y

# linked_list_values(x) # -> [ 'x', 'y' ]

# #! TEST_02
# q = Node("q")

# # q

# linked_list_values(q) # -> [ 'q' ]

# #! TEST_03
# linked_list_values(None) # -> [ ]
