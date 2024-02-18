# https://leetcode.com/problems/determine-if-two-strings-are-close/


# Two strings are considered close if you can attain one from the other using the following operations:

# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.

# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.


#! Example 1:
# Input: word1 = "abc", word2 = "bca"
# Output: true
# Explanation: You can attain word2 from word1 in 2 operations.
# Apply Operation 1: "abc" -> "acb"
# Apply Operation 1: "acb" -> "bca"

#! Example 2:
# Input: word1 = "a", word2 = "aa"
# Output: false
# Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

#! Example 3:
# Input: word1 = "cabbba", word2 = "abbccc"
# Output: true
# Explanation: You can attain word2 from word1 in 3 operations.
# Apply Operation 1: "cabbba" -> "caabbb"
# Apply Operation 2: "caabbb" -> "baaccc"
# Apply Operation 2: "baaccc" -> "abbccc"


# Constraints:

# 1 <= word1.length, word2.length <= 105
# word1 and word2 contain only lowercase English letters.


from collections import Counter

def closeStrings(word1, word2):
    # if len(word1) != len(word2):
    #     return False
    # freq1 = {}
    # freq2 = {}
    # for char in word1:
    #     freq1[char] = freq1.get(char, 0) + 1
    # for char in word2:
    #     freq2[char] = freq2.get(char, 0) + 1
    # return sorted(freq1.values()) == sorted(freq2.values()) and set(freq1.keys()) == set(freq2.keys())
    s1 = set(word1)
    s2 = set(word2)
    if s1 != s2:
        return False
    c1 = Counter(word1)
    c2 = Counter(word2)
    return sorted(c1.values()) == sorted(c2.values())


#! Example 1:
word1 = "abc"
word2 = "bca"
print(closeStrings(word1, word2))
# Output: true
# Explanation: You can attain word2 from word1 in 2 operations.
# Apply Operation 1: "abc" -> "acb"
# Apply Operation 1: "acb" -> "bca"

#! Example 2:
word1 = "a"
word2 = "aa"
print(closeStrings(word1, word2))
# Output: false
# Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

#! Example 3:
word1 = "cabbba"
word2 = "abbccc"
print(closeStrings(word1, word2))
# Output: true
# Explanation: You can attain word2 from word1 in 3 operations.
# Apply Operation 1: "cabbba" -> "caabbb"
# Apply Operation 2: "caabbb" -> "baaccc"
# Apply Operation 2: "baaccc" -> "abbccc"
