# https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75

# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.


#! Example 1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

#! Example 2:
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"

#! Example 3:
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""


# Constraints:

# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.

def gcdOfStrings(str1, str2):
    # check if concatenated strings are the same
    if str1 + str2 != str2 + str1:
        return ""
    while str1 != str2:
        if str1 > str2:
            str1 = str1[1:]
        else:
            str2 = str2[1:]
    return str1


#! Example 1:
str1 = "ABCABC"
str2 = "ABC"
print(gcdOfStrings(str1, str2))
# Output: "ABC"

#! Example 2:
str1 = "ABABAB"
str2 = "ABAB"
print(gcdOfStrings(str1, str2))
# Output: "AB"

#! Example 3:
str1 = "LEET"
str2 = "CODE"
print(gcdOfStrings(str1, str2))
# Output: ""
