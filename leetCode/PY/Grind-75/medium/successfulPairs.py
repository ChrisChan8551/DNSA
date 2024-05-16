# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/


# You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

# You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

# Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.


#! Example 1:
# Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
# Output: [4,0,3]
# Explanation:
# - 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
# - 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
# - 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
# Thus, [4,0,3] is returned.

#! Example 2:
# Input: spells = [3,1,2], potions = [8,5,8], success = 16
# Output: [2,0,2]
# Explanation:
# - 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
# - 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful.
# - 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful.
# Thus, [2,0,2] is returned.


# Constraints:

# n == spells.length
# m == potions.length
# 1 <= n, m <= 105
# 1 <= spells[i], potions[i] <= 105
# 1 <= success <= 1010
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 145.8K
# Submissions
# 340.8K
# Acceptance Rate
# 42.8%
# Topics
# Companies
# Hint 1
# Notice that if a spell and potion pair is successful, then the spell and all stronger potions will be successful too.
# Hint 2
# Thus, for each spell, we need to find the potion with the least strength that will form a successful pair.
# Hint 3
# We can efficiently do this by sorting the potions based on strength and using binary search.


#! brute force using nested loops. Multiply each spell by each potion. Count how many spells are higher than the threshold
def successfulPairs(spells, potions, success):
    n = len(spells)
    m = len(potions)
    result = []
    for i in range(n):
        count = 0
        for j in range(m):
            total = spells[i] * potions[j]
            # print(total)
            if total >= success:
                count += 1
        result.append(count)
    return result

#! more efficient is to sort the potions by strength, and then use binary search for threshold


def successfulPairs(spells, potions, success):
    n = len(spells)
    m = len(potions)

    def binary_search(spell):
        left, right = 0, len(potions) - 1
        while left <= right:
            mid = (left + right) // 2
            #! edge case if numbers are duplicate, it might return incorrect index, so need to keep looping through the numbers to find smallest index
            if spell * potions[mid] >= success:
                right = mid - 1
            elif spell * potions[mid] < success:
                left = mid + 1

        return left

    result = []
    potions.sort()
    for spell in spells:
        idx = binary_search(spell)
        result.append(m - idx)

    return result


#! Example 1:
spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
success = 7
print(successfulPairs(spells, potions, success))
# Output: [4,0,3]
# Explanation:
# - 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
# - 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
# - 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
# Thus, [4,0,3] is returned.

#! Example 2:
spells = [3, 1, 2]
potions = [8, 5, 8]
success = 16
print(successfulPairs(spells, potions, success))
# Output: [2,0,2]
# Explanation:
# - 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
# - 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful.
# - 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful.
# Thus, [2,0,2] is returned.
