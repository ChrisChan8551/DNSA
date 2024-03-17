# https://leetcode.com/problems/sort-characters-by-frequency/

# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.

# Example 1:

# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:

# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:

# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.


# Constraints:

# 1 <= s.length <= 5 * 105
# s consists of uppercase and lowercase English letters and digits.
from collections import Counter

#! bucket sort
def frequencySort(str):
    n = len(str)
    c = Counter(str)
    bucket = [[] for _ in range(n + 1)]
    for char, freq in c.items():
        bucket[freq].append(char)
    res = ''

    for freq in range(n, 0, -1):
        for char in bucket[freq]:
            res += freq * char
    return res


#!ChatGPT
# def frequencySort(str):
#     # Step 1: Create a dictionary to store character frequencies
#     char_freq = {}
#     for char in str:
#         char_freq[char] = char_freq.get(char, 0) + 1

#     # Step 2: Sort characters based on frequency in descending order
#     sorted_chars = sorted(char_freq, key=lambda x: char_freq[x], reverse=True)

#     # Step 3: Create a new string by concatenating characters
#     result = ''.join([char * char_freq[char] for char in sorted_chars])

#     return result

#! alternative method
def frequencySort(str):
    c = Counter(str)
    # Sort characters based on their frequency in descending order
    sorted_chars = sorted(c, key=c.get, reverse=True)
    # Build the result string by repeating characters according to their frequency
    result = ''
    for char in sorted_chars:
        result += char * c[char]
    #  Return the final sorted string
    return result

print(frequencySort("tree"))
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

print(frequencySort("cccaaa"))
# # Output: "aaaccc"
# # Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# # Note that "cacaca" is incorrect, as the same characters must be together.

# #! edge case
print(frequencySort("Aabb"))
# # Output: "bbAa"
# # Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
