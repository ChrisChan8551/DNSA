# Write a function, linked_list_find, that takes in the head of a linked list and a target value. The function should return a boolean indicating whether or not the linked list contains the target.

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

#! iterative
def linked_list_find(head, target):
    # transverse through the linked list
    current = head
    while current != None:
      # find if current val = target - return true
        if current.val == target:
            return True
      # if not, go to next node
        current = current.next
    # return false if nothing matches
    return False

#! recursion
def linked_list_find(head, target):
    # base case
    if head == None:
        return False
    if head.val == target:
        return True
    return linked_list_find(head.next, target)

# #! TEST_00
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")

# a.next = b
# b.next = c
# c.next = d

# # a -> b -> c -> d

# linked_list_find(a, "c") # True

# #! TEST_01
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")

# a.next = b
# b.next = c
# c.next = d

# # a -> b -> c -> d

# linked_list_find(a, "d") # True

# #! TEST_02
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")

# a.next = b
# b.next = c
# c.next = d

# # a -> b -> c -> d

# linked_list_find(a, "q") # False

# #! TEST_03
# node1 = Node("jason")
# node2 = Node("leneli")

# node1.next = node2

# # jason -> leneli

# linked_list_find(node1, "jason") # True

# #! TEST_04
# node1 = Node(42)

# # 42

# linked_list_find(node1, 42) # True

# #! TEST_05
# node1 = Node(42)

# # 42

# linked_list_find(node1, 100) # False
