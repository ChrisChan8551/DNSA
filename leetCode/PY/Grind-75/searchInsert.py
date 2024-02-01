# https://leetcode.com/problems/search-insert-position/

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4


# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104

#! binary search
def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left)//2
        print('mid: ', mid)
        print('left: ', left)
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left += 1
        else:
            right -= 1
    return left


# print(searchInsert([1, 3, 5, 6], 5))
# Output: 2
# print(searchInsert([1, 3, 5, 6], 2))
# Output: 1
# print(searchInsert([1, 3, 5, 6], 7))
# Output: 4
