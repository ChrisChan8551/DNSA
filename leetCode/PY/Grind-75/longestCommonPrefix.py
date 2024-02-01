# https://leetcode.com/problems/longest-common-prefix/

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

# def longestCommonPrefix(strs):
#     # if strs is empty return ''
#     if not strs:
#         return ""
#     # iterate through the first word
#     for i in range(len(strs[0])):
#         # Check if the character is common to all strings
#         for string in strs[1:]:
#             # once the characters don't match, then return slice of string
#             if i >= len(string) or string[i] != strs[0][i]:
#                 return strs[0][:i]
#     # If no mismatch is found, the entire first string is the common prefix
#     return strs[0]

def longestCommonPrefix(strs):
    common = ''
    # use the first word to compare with the rest of the word
    for i in range(len(strs[0])):
        for j in range(1, len(strs)):
            # stops if doesn't match
            if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                return common
            # otherwise add the character in common
        common += strs[0][i]
    return common


print(longestCommonPrefix(["flower", "flow", "flight"]))
# Output: "fl"

# print(longestCommonPrefix(["dog", "racecar", "car"]))
# # Output: ""
