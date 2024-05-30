# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.


# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.
def lengthOfLongestSubstring(s):
    #! Extending window problem
    window = set()
    # Max length variable
    maxLength = 0
    left, right = 0, 0
    # loop through the string
    while right < len(s):
        while s[right] in window:
            # check if right char in string is inside the window set.
            # if so remove the first char which is window left
            # window.discard(s[left]) - .discard() method does not raise any error if value is not found
            window.remove(s[left])
            # increment the left pointer
            left += 1
        # check and update maxLength
        # max Length of window = right - left + 1
        maxLength = (max(maxLength, right - left + 1))
        window.add(s[right])
        right += 1

    return maxLength
    # the window starts off with abc, but once it hits abca, we need to shorten the window by removing the first 'a', and keeping the window size at 3.
    # but once it hits bcb, the window shortens to 2

# def lengthOfLongestSubstring(s):
#     # 2 pointer method or window method
#     # go through the string and look for non consecutive characters
#     # assign SET characters that cannot appear more than once
#     # count max length of substring
#     maxLength = 0
#     start_idx = 0
#     subString = {}
#     for i, char in enumerate(s):
#         if char in subString and subString[char] >= start_idx:
#             start_idx = subString[char] + 1
#         currentLength = i - start_idx + 1
#         subString[char] = i
#         maxLength = max(maxLength, currentLength)
#     return maxLength


def lengthOfLongestSubstring(s):
    chars = set()
    left = right = longest = 0
    while right < len(s):
        if s[right] not in chars:
            chars.add(s[right])
            right += 1
            longest = max(longest, right-left)
        else:
            chars.remove(s[left])
            left += 1
    return longest

#algo academy way
def lengthOfLongestSubstring(s):
    chars = set()
    left = right = longest = 0
    for right in range(len(s)):
        while s[right] in chars:
            chars.remove(s[left])
            left += 1
        chars.add(s[right])
        longest = max(longest, right - left + 1)
    return longest

#! TEST 1
s = "abcabcbb"
print(lengthOfLongestSubstring(s))  # -> 3 "abc"
#! TEST 2
s = "bbbbb"
print(lengthOfLongestSubstring(s))  # -> 1 "b"
#! TEST 3
s = "pwwkew"
print(lengthOfLongestSubstring(s))  # -> 3 "wke"
