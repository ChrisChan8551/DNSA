# https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150


# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

# def isPalindrome(s):
# s = ''.join(s.split())
# result = []
# for i in range(len(s)):
#     char = s[i]
#     if char.isalnum():
#         result.append(char.lower())
# result = ''.join(result)
# return result == result[::-1]

def isPalindrome(s):
    result = ''.join(char.lower() for char in s if char.isalnum())
    return result == result[::-1]


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))
