# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

# You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

# Return the minimum number of steps to make t an anagram of s.

# An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.


#! Example 1:
# Input: s = "bab", t = "aba"
# Output: 1
# Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

#! Example 2:
# Input: s = "leetcode", t = "practice"
# Output: 5
# Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.

#! Example 3:
# Input: s = "anagram", t = "mangaar"
# Output: 0
# Explanation: "anagram" and "mangaar" are anagrams.


# Constraints:

# 1 <= s.length <= 5 * 104
# s.length == t.length
# s and t consist of lowercase English letters only.

# Hint 1
# Count the frequency of characters of each string.
# Hint 2
# Loop over all characters if the frequency of a character in t is less than the frequency of the same character in s then add the difference between the frequencies to the answer.


from collections import Counter
#! using Counter


# def minSteps(s, t):
#     # get the frequencies of letters on both strings
#     # compare the frequencies
#     # edge case is when frequency of the letter is None or Zero
#     countS, countT = Counter(s), Counter(t)
#     total = 0
#     # loop through object using destructuring
#     for k, v in countS.items():
#         # check letter from first string, and see if it is in the other string.
#         # if there is nothing then you freq = 0, just add the freq into the total instead.
#         num = countT.get(k)
#         if num is None:
#             total += v
#         elif num < v:
#             total += v - num
#         # if letter freq is less than string2 frequency, then subtract.
#     return total

#! using set

def minSteps(s, t):
    unique = set(s)
    total = 0
    for char in unique:
        countS = s.count(char)
        countT = t.count(char)
        if countT < countS:
            total += (countS - countT)
    return total


#! Example 1:
s = "bab"
t = "aba"
print(minSteps(s, t))
# Output: 1
# Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

#! Example 2:
s = "leetcode"
t = "practice"
print(minSteps(s, t))
# Output: 5
# Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.

#! Example 3:
s = "anagram"
t = "mangaar"
print(minSteps(s, t))
# Output: 0
# Explanation: "anagram" and "mangaar" are anagrams.
