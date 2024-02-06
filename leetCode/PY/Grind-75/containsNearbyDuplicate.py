# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.


# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false


# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 0 <= k <= 105

#! sliding window using 2 pointer
def containsNearbyDuplicate(nums, k):
    # sliding window problem.
    left = 0
    # initiate a set to track duplicate values
    window = set()
    # loop through all the numbers
    for right in range(len(nums)):
        if (right - left > k):
            window.discard(nums[left])
            left += 1
        if nums[right] in window:
            return True
        window.add(nums[right])
    return False

#! using dict, has better performance in this problem


def containsNearbyDuplicate(nums, k):
    mydict = {}
    for i in range(len(nums)):
        if nums[i] in mydict and abs(i-mydict[nums[i]]) <= k:
            return True
        mydict[nums[i]] = i
    return False

#! this has the best performance because it optimizes the lookup process by directly storing the most recent index of each number encountered in the array.


def containsNearbyDuplicate(nums, k):
    n = len(nums)
    idx = {}
    for i in range(n):
        if nums[i] in idx:
            if abs(idx[nums[i]]-1) <= k:
                return True
        idx[nums[i]] = i
    return False


print(containsNearbyDuplicate([1, 2, 3, 1], 3))  # Output: true
print(containsNearbyDuplicate([1, 0, 1, 1], 1))  # Output: true
print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # Output: false
