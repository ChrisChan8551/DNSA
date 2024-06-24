# https://leetcode.com/problems/3sum/?envType=study-plan-v2&envId=top-interview-150

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


#! Hint 1
# So, we essentially need to find three numbers x, y, and z such that they add up to the given value. If we fix one of the numbers say x, we are left with the two-sum problem at hand!

#! Hint 2
# For the two-sum problem, if we fix one of the numbers, say x, we have to scan the entire array to find the next number y, which is value - x where value is the input parameter. Can we change our array somehow so that this search becomes faster?

#! Hint 3
# The second train of thought for two-sum is, without changing the array, can we use additional space somehow? Like maybe a hash map to speed up the search?

#! Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

#! Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

#! Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.


# Constraints:
# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

def threeSum(nums):
    nums.sort()
    result = []
    n = len(nums)
    # this is setting the fixed first number
    for i in range(n - 2):
        # If the current element is the same as the previous element, skip it to avoid duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                # Skip duplicate elements to avoid duplicate triplets in the result
                while nums[left] == nums[left - 1] and left < right:
                    left += 1

    return result


#! Example 1:
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

#! Example 2:
nums = [0, 1, 1]
print(threeSum(nums))
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

#! Example 3:
nums = [0, 0, 0]
print(threeSum(nums))
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
