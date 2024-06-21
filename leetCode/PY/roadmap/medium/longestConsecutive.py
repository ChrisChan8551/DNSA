# https://leetcode.com/problems/longest-consecutive-sequence/

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.


#! Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

#! Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9


# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

def longestConsecutive(nums):
    # first need to determine the beginning of the sequence by checking if the current num - 1 is included in nums.
    # declare a set for nums so that it's O(1) lookup.
    # loop through the nums and check if nums - 1 is in the set.
    # if not, set the current length to 1
    # that initiates a secondary loop to check the subsequent numbers to see if it's in the set.
    # increase the length while the next number is greater than the previous
    # update max length
    if len(nums) == 0:
        return 0
    nums_set = set(nums)
    max_length = 1
    for num in nums_set:
        if num - 1 not in nums_set:
            current_length = 1
            while (num + current_length) in nums_set:
                current_length += 1
                max_length = max(max_length, current_length)
    return max_length


#! Example 1:
nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

#! Example 2:
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(longestConsecutive(nums))
# Output: 9

#! Example 3:
nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
# Output: 7
print(longestConsecutive(nums))

#! Example 4:
nums = [0]
print(len(nums))
print(longestConsecutive(nums))
# Output: 1
