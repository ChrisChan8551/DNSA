# https://leetcode.com/problems/the-number-of-beautiful-subsets/


# You are given an array nums of positive integers and a positive integer k.

# A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

# Return the number of non-empty beautiful subsets of the array nums.

# A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.


#! Example 1:
# Input: nums = [2,4,6], k = 2
# Output: 4
# Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
# It can be proved that there are only 4 beautiful subsets in the array [2,4,6].

#! Example 2:
# Input: nums = [1], k = 1
# Output: 1
# Explanation: The beautiful subset of the array nums is [1].
# It can be proved that there is only 1 beautiful subset in the array [1].


# Constraints:

# 1 <= nums.length <= 20
# 1 <= nums[i], k <= 1000

# Hint 1
# Sort the array nums and create another array cnt of size nums[i].
# Hint 2
# Use backtracking to generate all the beautiful subsets. If cnt[nums[i] - k] is positive, then it is impossible to add nums[i] in the subset, and we just move to the next index. Otherwise, it is also possible to add nums[i] in the subset, in this case, increase cnt[nums[i]], and move to the next index.
# Hint 3
# Bonus: Can you solve the problem in O(n log n)?


def beautifulSubsets(nums, k):
    #subset is a combination of numbers within a number
    pass


#! Example 1:
nums = [2, 4, 6]
k = 2
print(beautifulSubsets(nums, k))
# Output: 4
# Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
# It can be proved that there are only 4 beautiful subsets in the array [2,4,6].

#! Example 2:
nums = [1]
k = 1
print(beautifulSubsets(nums, k))
# Output: 1
# Explanation: The beautiful subset of the array nums is [1].
# It can be proved that there is only 1 beautiful subset in the array [1].
