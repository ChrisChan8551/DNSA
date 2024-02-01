# https://leetcode.com/problems/sort-an-array/

# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.


# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
# Example 2:

# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessarily unique.


# Constraints:

# 1 <= nums.length <= 5 * 104
# -5 * 104 <= nums[i] <= 5 * 104

#! Merge sort - recursive
def sortArray(nums):
    # base case - if length of nums < 2, return nums
    if len(nums) < 2:
        return nums

    mid = len(nums) // 2
    left = sortArray(nums[0:mid])  # 0 to mid
    right = sortArray(nums[mid::])  # mid to end

    return merge(left, right)


def merge(left, right):
    merged = []
    # pop left and right until there is no more.
    while len(left) and len(right):
        # compare if left is < right
        if (left[0] < right[0]):
            merged.append(left.pop(0))  # removes left element at [0]
        else:
            merged.append(right.pop(0))  # removes right element at [0]
    merged.extend(left)
    merged.extend(right)
    return merged


print(sortArray([5, 2, 3, 1]))
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

print(sortArray([5, 1, 1, 2, 0, 0]))
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessarily unique.
