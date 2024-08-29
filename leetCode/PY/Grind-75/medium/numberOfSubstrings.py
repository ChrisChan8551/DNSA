# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

# Given a string s consisting only of characters a, b and c.

# Return the number of substrings containing at least one occurrence of all these characters a, b and c.


#! Example 1:
# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).

#! Example 2:
# Input: s = "aaacb"
# Output: 3
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".

#! Example 3:
# Input: s = "abc"
# Output: 1


# Constraints:
# 3 <= s.length <= 5 x 10^4
# s only consists of a, b or c characters.

#! Hint 1
# For each position we simply need to find the first occurrence of a/b/c on or after this position.
#! Hint 2
# So we can pre-compute three link-list of indices of each a, b, and c.


def numberOfSubstrings(s):
    return


#! Example 1:
s = "abcabc"
print(numberOfSubstrings(s))
# Output: 10
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).

#! Example 2:
s = "aaacb"
print(numberOfSubstrings(s))
# Output: 3
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".

#! Example 3:
s = "abc"
print(numberOfSubstrings(s))
# Output: 1
