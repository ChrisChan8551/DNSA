# https://leetcode.com/problems/longest-repeating-character-replacement/

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.


#! Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

#! Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.


# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length

# def characterReplacement(s, k):
#     freq = {}
#     left = max_count = 0
#     n = len(s)
#     for right in range(n):
#         if s[right] not in freq:
#             freq[s[right]] = 1
#         else:
#             freq[s[right]] += 1
#         max_count = max(max_count, freq[s[right]])
#         current_length = right - left + 1
#         if current_length - max_count > k:
#             freq[s[left]] -= 1
#             left += 1
#     return n - left

from collections import defaultdict


def characterReplacement(s, k):
    freq = defaultdict(int)
    n = len(s)
    max_freq = left = max_length = 0
    for right in range(n):
        freq[s[right]] += 1
        max_freq = max(max_freq, freq[s[right]])
        if right - left + 1 - max_freq > k:
            freq[s[left]] -= 1
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length


#! Example 1:
s = "ABAB"
k = 2
print(characterReplacement(s, k))
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

#! Example 2:
s = "AABABBA"
k = 1
print(characterReplacement(s, k))
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
