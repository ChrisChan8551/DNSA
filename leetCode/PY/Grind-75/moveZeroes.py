# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in -place without making a copy of the array.


# Example 1:

# Input: nums = [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]
# Example 2:

# Input: nums = [0]
# Output: [0]


# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1


def moveZeroes(nums):
    right = 0
    # Iterate through the array
    for i in range(len(nums)):
        # If the current element is non-zero, move it to the position pointed by right
        if nums[i] != 0:
            nums[i], nums[right] = nums[right], nums[i]
            right += 1
    return nums


#! Example 1:
nums = [0, 1, 0, 3, 12]
# Output: [1,3,12,0,0]
print(moveZeroes(nums))

#! Example 2:
# nums = [0]
# Output: [0]
# print(moveZeroes(nums))
