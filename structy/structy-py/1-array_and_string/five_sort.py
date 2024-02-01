# Write a function, five_sort, that takes in a list of numbers as an argument. The function should rearrange elements of the list such that all 5s appear at the end. Your function should perform this operation in-place by mutating the original list. The function should return the list.

# Elements that are not 5 can appear in any order in the output, as long as all 5s are at the end of the list.


# #! Brute force
# def five_sort(nums):
#     index = 0
#     for _ in range(len(nums)):
#         if nums[index] == 5:
#             nums.pop(index)
#             nums.append(5)
#         else:
#             index += 1
#     return nums

# def five_sort(nums):
#     # transverse through the array to look for 5s
#     # move all the 4s at the end of the array
#     # use 2 pointer method to make this an O(n) runtime
#     i = 0  # set i starting to first char of array
#     j = len(nums)-1  # set j to the end of the array

#     # loop through the array
#     while i < j:
#         # compare if j pointer is a 5, if so leave it alone, and decrease j by 1
#         if (nums[j] == 5):
#             j -= 1

#         # compare if i pointer is a 5, and j pointer is not a 5, swap positions
#         elif (nums[i] == 5 and nums[j] != 5):
#             num1 = nums[i]
#             num2 = nums[j]
#             nums[i] = num2
#             nums[j] = num1
#             i += 1
#             #! OR
#             #! nums[i], nums[j] = nums[j], nums[i]
#         else:
#             # if neither then increase i by 1
#             i += 1
#         # return nums at the end
#     return nums

# #! TEST_00
# print(five_sort([12, 5, 1, 5, 12, 7]))
# -> [12, 7, 1, 12, 5, 5]

# #! TEST_01
# print(five_sort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5]))
# # -> [2, 2, 10, 6, 1, 5, 5, 5, 5, 5]

# #! TEST_02
# print(five_sort([5, 5, 5, 1, 1, 1, 4]))
# # -> [4, 1, 1, 1, 5, 5, 5]

# #! TEST_03
# print(five_sort([5, 5, 6, 5, 5, 5, 5]))
# # -> [6, 5, 5, 5, 5, 5, 5]

# #! TEST_04
# print(five_sort([5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5]))
# # -> [4, 1, 2, 1, 2, 3, 5, 5, 5, 5, 5, 5, 5, 5]

# #! TEST_05
# fours = [4] * 20000
# fives = [5] * 20000
# nums = fours + fives
# print(five_sort(nums))
# # twenty-thousand 4s followed by twenty-thousand 5s
# # -> [4, 4, 4, 4, ..., 5, 5, 5, 5]
