
# Write a function, get_node_value, that takes in the head of a linked list and an index. The function should return the value of the linked list at the specified index.

# If there is no node at the given index, then return None.

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

#! iterative
# def get_node_value(head, index):
#     # keep track of index
#     count = 0
#     current = head
#     # transverse nodes and stop at the index
#     #return the value
#     while current != None:
#         if count == index:
#             return current.val
#         else:
#             count += 1
#             current = current.next
#     #if index is not found return None
#     return None

#! recursion
def get_node_value(head, index):
    # base case
    if head is None:
        return None
    if index == 0:
        return head.val
    return get_node_value(head.next, index-1)

# #! TEST_00
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")

# a.next = b
# b.next = c
# c.next = d

# # a -> b -> c -> d

# get_node_value(a, 2) # 'c'

# #! TEST_01
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")

# a.next = b
# b.next = c
# c.next = d

# # a -> b -> c -> d

# get_node_value(a, 3) # 'd'

# #! TEST_02
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")

# a.next = b
# b.next = c
# c.next = d

# # a -> b -> c -> d

# get_node_value(a, 7) # None

# #! TEST_03
# node1 = Node("banana")
# node2 = Node("mango")

# node1.next = node2

# # banana -> mango

# get_node_value(node1, 0) # 'banana'

# #! TEST_04
# node1 = Node("banana")
# node2 = Node("mango")

# node1.next = node2

# # banana -> mango

# get_node_value(node1, 1) # 'mango'
