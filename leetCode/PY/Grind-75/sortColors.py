# https://leetcode.com/problems/sort-colors/

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.


# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]


# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.

#! Bucket sort
# only 3 numbers to use so we can use hash table or array
# in this case we can just use array with indices
# this is sort of like a key value pair
# 2,0,2,1,1,0
# [2][2][2] -> have 2 - 0's, 2 - 1's, 2 - 2's
# [0][1][2] -> indices
# loop through and update the array -> 0,0,1,1,2,2


def sortColors(nums):
    counts = [0] * 3  # - > array with 3 zeros

    # counts how many number, and assigns to the indices
    for n in nums:
        counts[n] += 1

    print(counts)
    i = 0

    for n in range(len(counts)): # going through each number 0,1,2
        for c in range(counts[n]):  # count of frequencies of each number
            nums[i] = n # replaces number
            i += 1
    print(nums)

print(sortColors([2, 0, 2, 1, 1, 0]))
# Output: [0,0,1,1,2,2]

print(sortColors([2, 0, 1]))
# Output: [0,1,2]
