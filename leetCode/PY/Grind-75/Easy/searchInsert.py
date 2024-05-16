# https://leetcode.com/problems/search-insert-position/

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

#! Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

#! Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

#! Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4


# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104

def searchInsert(nums, target):
    # O (n log n) usually means binary solution.
    # declare left, and right variable. Left is usually 0, and right is length of array - 1.
    # declare while loop, while left is less than or equal to the right side
    # declare a mid point
    # if mid point is less than target, set left pointer to mid + 1
    # if mid point is greater than target, set right pointer to mid - 1
    # finally return left pointer to determine insertion of index
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


#! Example 1:
nums = [1, 3, 5, 6]
target = 5
print(searchInsert(nums, target))
# Output: 2

#! Example 2:
nums = [1, 3, 5, 6]
target = 2
print(searchInsert(nums, target))
# Output: 1

#! Example 3:
nums = [1, 3, 5, 6]
target = 7
print(searchInsert(nums, target))
# Output: 4
