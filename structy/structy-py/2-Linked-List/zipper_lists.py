
# Write a function, zipper_lists, that takes in the head of two linked lists as arguments. The function should zipper the two lists together into single linked list by alternating nodes. If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. The function should return the head of the zippered linked list.

# Do this in-place, by mutating the original Nodes.

# You may assume that both input lists are non-empty.

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# def zipper_lists(head_1, head_2):
#     # 2 pointers
#     current1 = head_1.next
#     current2 = head_2
#     # alternate pointers so need to have a counter to keep track
#     count = 0
#     tail = head_1
#     while current1 is not None and current2 is not None:
#         # if odd goto current1
#         if count % 2 == 1:
#             tail.next = current1
#             current1 = current1.next
#         # if even goto current2
#         if count % 2 == 0:
#             tail.next = current2
#             current2 = current2.next
#         # assign tail to next tail pointer
#         tail = tail.next
#         count += 1
#     # if either list is shorter than the other. Return the remaining of the list
#     if (current1 is not None):
#         tail.next = current1
#     if (current2 is not None):
#         tail.next = current2

#     return head_1

#! recursive
def zipper_lists(head_1, head_2):
    # base case
    if head_1 is None and head_2 is None:
        return None
    if (head_1 is not None):
        return head_2
    if (head_2 is not None):
        return head_1
    #tail.next = current.next
    next1 = head_1.next
    next2 = head_2.next

    head_2.next = zipper_lists(next1, next2)


# #! TEST_00
# a = Node("a")
# b = Node("b")
# c = Node("c")
# a.next = b
# b.next = c
# # a -> b -> c

# x = Node("x")
# y = Node("y")
# z = Node("z")
# x.next = y
# y.next = z
# # x -> y -> z

# zipper_lists(a, x)
# # a -> x -> b -> y -> c -> z

# #! TEST_01
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
# # a -> b -> c -> d -> e -> f

# x = Node("x")
# y = Node("y")
# z = Node("z")
# x.next = y
# y.next = z
# # x -> y -> z

# zipper_lists(a, x)
# # a -> x -> b -> y -> c -> z -> d -> e -> f

# #! TEST_02
# s = Node("s")
# t = Node("t")
# s.next = t
# # s -> t

# one = Node(1)
# two = Node(2)
# three = Node(3)
# four = Node(4)
# one.next = two
# two.next = three
# three.next = four
# # 1 -> 2 -> 3 -> 4

# zipper_lists(s, one)
# # s -> 1 -> t -> 2 -> 3 -> 4

# #! TEST_03
# w = Node("w")
# # w

# one = Node(1)
# two = Node(2)
# three = Node(3)
# one.next = two
# two.next = three
# # 1 -> 2 -> 3

# zipper_lists(w, one)
# # w -> 1 -> 2 -> 3

# #! TEST_04
# one = Node(1)
# two = Node(2)
# three = Node(3)
# one.next = two
# two.next = three
# # 1 -> 2 -> 3

# w = Node("w")
# # w

# zipper_lists(one, w)
# # 1 -> w -> 2 -> 3
