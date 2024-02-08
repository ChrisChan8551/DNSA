# https://leetcode.com/problems/isomorphic-strings/

# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


#!Example 1:
# Input: s = "egg", t = "add"
# Output: true

#!Example 2:
# Input: s = "foo", t = "bar"
# Output: false

#!Example 3:
# Input: s = "paper", t = "title"
# Output: true


# Constraints:

# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.


def isIsomorphic(s, t):
    pairA = {}
    pairB = {}
    for i in range(len(s)):
        charA, charB = s[i], t[i]
        if charA not in pairA and charB not in pairB:
            pairA[charA] = charB
            pairB[charB] = charA
            # print('pairA[charA]',pairA[charA], 'charB',charB)

        else:
            # print(pairA[charA], charB)
            if pairA.get(charA) != charB or pairB.get(charB) != charA:
                return False
    return True

# #!Example 1:
s = "egg"
t = "add"
print(isIsomorphic(s, t))
# # Output: true
# #!Example 2:
s = "foo"
t = "bar"
print(isIsomorphic(s, t))
# Output: false

# #!Example 3:
# s = "paper"
# t = "title"
# print(isIsomorphic(s, t))
# # Output: true
