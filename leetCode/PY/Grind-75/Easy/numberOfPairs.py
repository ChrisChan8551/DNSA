# https://leetcode.com/problems/find-the-number-of-good-pairs-i/

# You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively. You are also given a positive integer k.

# A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).

# Return the total number of good pairs.


# Constraints:

# 1 <= n, m <= 50
# 1 <= nums1[i], nums2[j] <= 50
# 1 <= k <= 50

# Hint 1
# The constraints are small. Check all pairs.

#! brute force
from collections import defaultdict


def numberOfPairs(nums1, nums2, k):
    count = 0
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] % (nums2[j] * k) == 0:
                count += 1
    return count

#! O(n)


def numberOfPairs(nums1, nums2, k):
    count = 0
    hash_map = defaultdict(int)
    # Create a divisor map from nums2 by multiplying each element by k
    for num in nums2:
        hash_map[num * k] += 1

    # For each element in nums1, check if it's divisible by any of the divisors
    for num in nums1:
        for divisor in hash_map:
            if num % divisor == 0:
                count += hash_map[divisor]
    return count


#! Example 1:
nums1 = [1, 3, 4]
nums2 = [1, 3, 4]
k = 1
print(numberOfPairs(nums1, nums2, k))

# Output: 5

# Explanation:

# The 5 good pairs are (0, 0), (1, 0), (1, 1), (2, 0), and (2, 2).

#! Example 2:
nums1 = [1, 2, 4, 12]
nums2 = [2, 4]
k = 3
print(numberOfPairs(nums1, nums2, k))

# Output: 2

# Explanation:

# The 2 good pairs are (3, 0) and (3, 1).
