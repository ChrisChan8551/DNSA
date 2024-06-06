# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


#! Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#! Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

#! Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]


# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109

#! Only one valid answer exists.

# Hint 1
# A really brute force way would be to search for all possible pairs of numbers but that would be too slow. Again, it's best to try out brute force solutions for just for completeness. It is from these brute force solutions that you can come up with optimizations.
# Hint 2
# So, if we fix one of the numbers, say x, we have to scan the entire array to find the next number y which is value - x where value is the input parameter. Can we change our array somehow so that this search becomes faster?
# Hint 3
# The second train of thought is, without changing the array, can we use additional space somehow? Like maybe a hash map to speed up the search?

#! brute force
def twoSum(nums, target):
    N = len(nums)
    for i in range(N):
        for j in range(i + 1, N):
            if nums[i]+nums[j] == target:
                return [i, j]


def twoSum(nums, target):
    # using hashmap
    seen = {}
    # declare hashmap to keep track of index seen
    # loop through nums
    # we can shorten the search by looking for complement number if we subtract target from current number
    N = len(nums)
    for i in range(N):
        comp = target - nums[i]
        # check if comp number is in seen, if so, return the index, and i
        if comp in seen:
            return [seen[comp], i]
        # else set the current number with associated index in seen.
        seen[nums[i]] = i


#! Example 1:
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#! Example 2:
nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))
# Output: [1,2]

#! Example 3:
nums = [3, 3]
target = 6
print(twoSum(nums, target))
# Output: [0,1]
