# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/?envType=study-plan-v2&envId=leetcode-75

# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.


#! Example 1:
# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

#! Example 2:
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

#! Example 3:
# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.

def longestSubarray(nums):
    pass


#! Example 1:
nums = [1, 1, 0, 1]
print(longestSubarray(nums))
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

#! Example 2:
nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
print(longestSubarray(nums))
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

#! Example 3:
nums = [1, 1, 1]
print(longestSubarray(nums))
# Output: 2
# Explanation: You must delete one element.
