# https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=leetcode-75


# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


#! Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true

#! Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false


# Constraints:

# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.


# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?

#! 2 pointer solution
def isSubsequence(s, t):
    # set left point to  loop through the s string, and right pointer through the t string
    # if char from left equals to the right,then increase left pointer by 1
    # return true if left pointer reaches length of s, else return false
    # edge case if length of s is 0, return true
    # or if length of t is less than length of s, return false

    left, right = 0, 0
    if len(s) > len(t):
        return False
    if len(s) == 0:
        return True
    while right < len(t):
        if t[right] == s[left]:
            left += 1
        right += 1
        if left == len(s):
            return True
    return False

# def isSubsequence(s, t):
#     left, right = 0, 0
#     # if len(t) < len(s):
#     #     return False
#     # if not s:
#     #     return True
#     while left < len(s) and right < len(t):
#         if s[left] == t[right]:
#             left += 1
#         right += 1

#     return left == len(s)


#! Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true

#! Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false
