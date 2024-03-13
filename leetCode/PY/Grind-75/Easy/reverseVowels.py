# https://leetcode.com/problems/reverse-vowels-of-a-string/

# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


# Example 1:
# Input: s = "hello"
# Output: "holle"

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"


# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.


def reverseVowels(s):
    # create a set of vowels both lower and uppercase and check it against the string
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    # split string into a list
    s = list(s)
    left = 0
    right = len(s)-1

    # iterate through the string and look for vowels. if both left and right are vowels, then switch positions
    while left < right:
        # print(s[left])
        # left += 1
        # print(s[right-1])
        # right -= 1
        if s[left] not in vowels:
            left += 1
        if s[right] not in vowels:
            right -= 1
        if s[left] in vowels and s[right] in vowels:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    return ''.join(s)
    # use 2 pointer strategies such as left and right pointer.
    # return new string


#! Example 1:
s = "hello"
# Output: "holle"
print(reverseVowels(s))
#! Example 2:
s = "leetcode"
# Output: "leotcede"
print(reverseVowels(s))
