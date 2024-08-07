# https://leetcode.com/problems/replace-all-digits-with-characters/

# You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices.

# There is a function shift(c, x), where c is a character and x is a digit, that returns the xth character after c.

# For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
# For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]).

# Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.


# Example 1:
# Input: s = "a1c1e1"
# Output: "abcdef"
# Explanation: The digits are replaced as follows:
# - s[1] -> shift('a',1) = 'b'
# - s[3] -> shift('c',1) = 'd'
# - s[5] -> shift('e',1) = 'f'

# Example 2:
# Input: s = "a1b2c3d4e"
# Output: "abbdcfdhe"
# Explanation: The digits are replaced as follows:
# - s[1] -> shift('a',1) = 'b'
# - s[3] -> shift('b',2) = 'd'
# - s[5] -> shift('c',3) = 'f'
# - s[7] -> shift('d',4) = 'h'


# Constraints:

# 1 <= s.length <= 100
# s consists only of lowercase English letters and digits.
# shift(s[i-1], s[i]) <= 'z' for all odd indices i.

# def replace_digits(s):
#     if len(s) == 1:
#         return s
#     characters = list(s)
#     for i in range(1, len(s), 2):
#         char = ord(s[i - 1]) + int(s[i])
#         characters[i] = chr(char)
#     return ''.join(characters)


# def replace_digits(s):
#     result = list(s)
#     for i in range(1, len(s), 2):
#         prev_char = result[i - 1]
#         x = int(result[i])
#         alphabet = "abcdefghijklmnopqrstuvwxyz"
#         idx = (alphabet.index(prev_char) + x) % 26
#         result[i] = alphabet[idx]
#     return ''.join(result)


def replace_digits(s):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    result = ''
    for i in range(len(s)):
        if s[i].isdigit():
            result += alphabet[alphabet.index(s[i - 1]) + int(s[i])]
        else:
            result += s[i]
    return result


print(replace_digits("a1c1e1"))
# Output: "abcdef"
# Explanation: The digits are replaced as follows:
# - s[1] -> shift('a',1) = 'b'
# - s[3] -> shift('c',1) = 'd'
# - s[5] -> shift('e',1) = 'f'

print(replace_digits("a1b2c3d4e"))
# # Output: "abbdcfdhe"
# # Explanation: The digits are replaced as follows:
# # - s[1] -> shift('a',1) = 'b'
# # - s[3] -> shift('b',2) = 'd'
# # - s[5] -> shift('c',3) = 'f'
# # - s[7] -> shift('d',4) = 'h'
