# https://leetcode.com/problems/check-if-the-sentence-is-pangram/

# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.


# Example 1:

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.
# Example 2:

# Input: sentence = "leetcode"
# Output: false


# Constraints:

# 1 <= sentence.length <= 1000
# sentence consists of lowercase English letters.

def checkIfPangram(sentence):
    # check if length of 26, otherwise return false
    # alphabet has 26, and it's in a certain
    # sort the sentence
    # assign as the alphabet
    if (len(sentence) < 26):
        return False

    character = {}
    var2 = 'abcdefghijklmnopqrstuvwxyz'
    for char in var2:
        if char not in character:
            character[char] = 1
    for char2 in sentence:
        if char2 in character:
            character[char2] -= 1  # true
    for key in character:
        if character[key] == 1:
            return False
    return True


# example1
print(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
# Output: true

print(checkIfPangram("leetcode"))
# Output: false
