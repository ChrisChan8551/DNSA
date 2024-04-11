# https://leetcode.com/problems/find-and-replace-pattern/

# Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

# A word matches the pattern if there exists a permutation of letters p_char so that after replacing every letter x in the pattern with p_char(x), we get the desired word.

# Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.


#! Example 1:
# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.

#! Example 2:
# Input: words = ["a","b","c"], pattern = "a"
# Output: ["a","b","c"]


# Constraints:

# 1 <= pattern.length <= 20
# 1 <= words.length <= 50
# words[i].length == pattern.length
# pattern and words[i] are lowercase English letters.


def findAndReplacePattern(words, pattern):
    # use dictionary to keep track of letter to letter
    # map each character in word, if there's a contradiction, then it's false. Do not add in result.
    # if no contradictions then add to results

    #! helper function to check if the current word matches the pattern
    def _isMatch(word):
        # need to check both directions so create 2 dicts.
        word_to_pattern = {}
        pattern_to_word = {}
        # this is easier method than isomorphic solution because it gives you access to both w_char,p_char.
        for w_char, p_char in zip(word, pattern):
            # check if the letters are in the dicts, if not add to the dict.
            if w_char not in word_to_pattern:
                word_to_pattern[w_char] = p_char
            if p_char not in pattern_to_word:
                pattern_to_word[p_char] = w_char
            # cross check the word letters with pattern letters. Return False when first letter doesn't match.
            if word_to_pattern[w_char] != p_char or pattern_to_word[p_char] != w_char:
                return False
        return True

    result = []
    for word in words:
        if _isMatch(word):
            result.append(word)

    return result


#! Example 1:
words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
pattern = "abb"
print(findAndReplacePattern(words, pattern))
# Output: ["mee","aqq"]
# a -> m .....  a -> a
# b -> e .....  b -> q
# b -> e .....  b -> q

# Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.

#! Example 2:
words = ["a", "b", "c"]
pattern = "a"
print(findAndReplacePattern(words, pattern))
# Output: ["a","b","c"]
