# https://leetcode.com/problems/max-consecutive-ones-iii/


# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.


#! Example 1:
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

#! Example 2:
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


# Constraints:
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length

def longestOnes(nums, k):
    # sliding window problem
    # find max length of subarray where all digits can be 1's if we flip at most k number of zeroes
    # extend window until we find max length or breaks the condition
    left = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            k -= 1
        if k < 0:
            if nums[left] == 0:
                k += 1
            left += 1
    return right - left + 1


def longestOnes(nums, k):
    left = 0
    max_length = 0
    zeroes = 0
    for right, n in enumerate(nums):
        if n == 0:
            zeroes += 1

        while zeroes > k:
            if nums[left] == 0:
                zeroes -= 1
            left += 1

        sub_length = right - left + 1
        max_length = max(max_length, sub_length)

    return max_length


#! Example 1:
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
print(longestOnes(nums, k))
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# #! Example 2:
# nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
# k = 3
# print(longestOnes(nums, k))
# # Output: 10
# # Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# # Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
