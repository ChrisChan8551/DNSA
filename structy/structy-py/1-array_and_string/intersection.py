# Write a function, intersection, that takes in two lists, a,b, as arguments. The function should return a new list containing elements that are in both of the two lists.

# You may assume that each input list does not contain duplicate elements.


#! brute force O(n^2) - large numbers will take too long and time out
# def intersection(a, b):
#     # assign result array
#     result = []
#     # transverse through first array, and compare with second array
#     for numsa in a:
#         for numsb in b:
#             # print('numsa:', numsa)
#             # print('numsb:', numsb)
#             if (numsa == numsb):
#                 result.append(numsa)
#             # if number matches, then push into result array
#     # return final array
#     return result

#! using set
def intersection(a, b):
    # to improve time complexity store first array into a Set which is O(1).
    result = []
    # declare variable for a set
    # for num in a:
    #     compare.add(num)
    #! you can make a set of a with the below instead of looping through
    compare = set(a)
    for num in b:
        if num in compare:
            # compare the second array with the set and add the result array
            result.append(num)
    return result

#! compressing loop into single return function
# def intersection(a, b):
#     compare = set(a)
#     return [item for item in b if item in compare]


# #!TEST_00
print(intersection([4, 2, 1, 6], [3, 6, 9, 2, 10]))  # -> [2,6]

# #!TEST_01
print(intersection([2, 4, 6], [4, 2]))  # -> [2,4]

# #!TEST_02
print(intersection([4, 2, 1], [1, 2, 4, 6]))  # -> [1,2,4]

# #!TEST_03
print(intersection([0, 1, 2], [10, 11]))  # -> []

# #!TEST_04
# a = [i for i in range(0, 50000)]
# b = [i for i in range(0, 50000)]
# print(intersection(a, b))  # -> [0,1,2,3,..., 49999]
