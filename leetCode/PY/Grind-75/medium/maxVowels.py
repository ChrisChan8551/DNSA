# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.


#! Example 1:
# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.

#! Example 2:
# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.

#! Example 3:
# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.


# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.
# 1 <= k <= s.length

def maxVowels(s, k):
    vowels = 'aeiou'
    maxVowels=0
    count=0
    # print(s)
    for right in range(len(s)-k+1):
        sub = s[right:right + k]
        count=0
        for char in sub:
            # print('sub: ',sub,char)
            if char in vowels:
                count += 1
            maxVowels = max(maxVowels, count)
            if maxVowels == k:
                return maxVowels
    return maxVowels



#! Example 1:
s = "abciiidef"
k = 3
print(maxVowels(s, k))
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.

#! Example 2:
s = "aeiou"
k = 2
print(maxVowels(s, k))
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.

#! Example 3:
s = "leetcode"
k = 3
print(maxVowels(s, k))
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.
