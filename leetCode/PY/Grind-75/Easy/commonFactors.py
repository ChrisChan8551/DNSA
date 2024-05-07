# https://leetcode.com/problems/number-of-common-factors/

# Given two positive integers a and b, return the number of common factors of a and b.

# An integer x is a common factor of a and b if x divides both a and b.


#! Example 1:
# Input: a = 12, b = 6
# Output: 4
# Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.

#! Example 2:
# Input: a = 25, b = 30
# Output: 2
# Explanation: The common factors of 25 and 30 are 1, 5.


# Constraints:

# 1 <= a, b <= 1000

# Hint 1
# For each integer in range [1,1000], check if it’s divisible by both A and B.

def commonFactors(a, b):
    count = 0
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            count += 1
    return count


#! Example 1:
a = 12
b = 6
print(commonFactors(a, b))
# Output: 4
# Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.

#! Example 2:
a = 25
b = 30
print(commonFactors(a, b))
# Output: 2
# Explanation: The common factors of 25 and 30 are 1, 5.
