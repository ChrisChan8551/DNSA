# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.


# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1


# Constraints:

# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.

# #! brute force
# def search(self, nums, target):
#     for i in range(len(nums)):
#         if nums[i] == target:
#             return i
#     return -1
#

# #! iterative binary search method
# def search(self, nums, target):
#     left = 0
#     right = len(nums)-1
#     while (left <= right):
#         # find the mid point of the array
#         mid = left + (right - left) // 2
#         # if nums[mid] matches target then return the mid
#         if nums[mid] == target:
#             return mid
#         # if less than target then increase left
#         elif nums[mid] < target:
#             left = mid+1
#         # else target is on closer to right side, then subtract right
#         else:
#             right = mid-1
#     return -1

#! recursive binary search
def search(nums, target):
    def recurse(left, right):
        if left >= right:
            return right if nums[right] == target else -1
        pivot = left + (right - left)//2

        if nums[pivot] == target:
            return pivot
        elif target < nums[pivot]:
            return recurse(left, pivot-1)
        else:
            return recurse(pivot + 1, right)
    return recurse(0, len(nums)-1)



print(search([-1, 0, 3, 5, 9, 12], 9))
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

print(search([-1, 0, 3, 5, 9, 12], 2))
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
