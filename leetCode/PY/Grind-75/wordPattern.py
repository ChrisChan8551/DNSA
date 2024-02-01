# https://leetcode.com/problems/word-pattern/?envType=study-plan-v2&envId=top-interview-150

# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.


# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false


# Constraints:

# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.

#! medium performance
def wordPattern(pattern, s):
    words = s.split()  # Split the input string 's' into a list of words.
    char = {}          # Create an empty dictionary to store the mapping from characters to words.
    strings = {}       # Create an empty dictionary to store the mapping from words to characters.

    if len(pattern) != len(words):
        return False    # If the length of the pattern is not equal to the number of words, return False.

    for i in range(len(pattern)):
        if pattern[i] not in char:  # If the current character is not already in the 'char' dictionary.
            if words[i] in strings:
                return False  # If the current word has been mapped to a different character before, return False.
            char[pattern[i]] = words[i]  # Map the current character to the current word.
            strings[words[i]] = pattern[i]  # Map the current word to the current character.
        else:
            if char[pattern[i]] != words[i]:
                return False  # If the current character has been mapped to a different word before, return False.

    return True  # If the loop completes without issues, return True.

#! best performance
def wordPattern(pattern, s):
    words = s.split()

    if len(pattern) != len(words):
        return False

    char_to_word = {}
    word_to_char = {}

    for char, word in zip(pattern, words):
        if char_to_word.get(char, word) != word or word_to_char.get(word, char) != char:
            return False
        char_to_word[char] = word
        word_to_char[word] = char

    return True

print(wordPattern("abba", "dog cat cat dog"))
print(wordPattern("abba", "dog cat cat fish"))
# print(wordPattern("aaaa", "dog cat cat dog"))
