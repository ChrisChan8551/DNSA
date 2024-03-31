# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

# Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).


#! Example 1:
# Input: nums = [3,4,5,2]
# Output: 12
# Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.

#! Example 2:
# Input: nums = [1,5,4,5]
# Output: 16
# Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.

#! Example 3:
# Input: nums = [3,7]
# Output: 12


# Constraints:
# 2 <= nums.length <= 500
# 1 <= nums[i] <= 10^3


#! brute force
def maxProduct(nums):
    # setup 2 loops
    # go through all the combinations and find the max product
    maxProduct = 0
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            maxProduct = max(maxProduct, (nums[i] - 1)*(nums[j] - 1))
    return maxProduct

#! using sorted
def maxProduct(nums):
    #when you're looking to get the max prodcuct using only 2 numbers.
    #sort the array, and select the last 2 numbers.
    nums = sorted(nums)
    return (nums[-2] - 1) * (nums[-1] - 1)


#! Example 1:
nums = [3, 4, 5, 2]
print(maxProduct(nums))
# Output: 12
# Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.

#! Example 2:
nums = [1, 5, 4, 5]
print(maxProduct(nums))
# Output: 16
# Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.

#! Example 3:
nums = [3, 7]
print(maxProduct(nums))
# Output: 12
