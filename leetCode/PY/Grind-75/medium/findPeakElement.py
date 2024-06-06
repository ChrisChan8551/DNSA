# https://leetcode.com/problems/find-peak-element/

# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.


# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.


# Constraints:

# 1 <= nums.length <= 1000
# -231 <= nums[i] <= 231 - 1
# nums[i] != nums[i + 1] for all valid i.

#! O(n)
# def findPeakElement(nums):
#     max_num = max(nums)
#     return nums.index(max_num)

#! O(log n) solution indicates binary search
#! 2 pointer solution
# def findPeakElement(nums):
#     # initialize left and right pointer. Right pointer is at the end of the array. Left is at the beginning.
#     left, right = 0, len(nums) - 1
#     # loop through array while left is less than right
#     while left < right:
#         # perform binary search by first finding the mid point
#         mid = left + (right - left) // 2
#         # if the element to the right of mid is greater than move left pointer to mid
#         if nums[mid] < nums[mid + 1]:
#             left = mid + 1
#         else:
#             # else right pointer moves to mid because the number we're looking for is left of mid.
#             right = mid
#     # return the left pointer after the while loop ends. It should be the max number.
#     return left

# #! recursive
# #! O(log n)
# def findPeakElement(nums):
#     def _search(left, right):
#         if left == right:
#             return left

#         mid = left + (right - left) // 2
#         if nums[mid] < nums[mid + 1]:
#             return _search(mid + 1, right)
#         else:
#             return _search(left, mid)
#     return _search(0, len(nums) - 1)

# print(findPeakElement([1,2,3,1]))
# # Output: 2

# print(findPeakElement([1,2,1,3,5,6,4]))
# # Output: 5


def findPeakElement(nums):
    # O log n solution usually means binary or heap solution.
    #! You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
    # this means that a value on the edge will always be considered greater than out of bounds
    # check left and right values to see if it's a peak
    # if it's not a peak, go in the direction of the upward slope.
    # eventually the slope will go down, and that means the peak is found
    left, right = 0, len(nums)-1
    while left < right:
        # use this to prevent number overflow
        mid = left + ((right - left) // 2)
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left


print(findPeakElement([1, 2, 3, 1]))
# Output: 2

print(findPeakElement([1, 2, 1, 3, 5, 6, 4]))
# Output: 5
