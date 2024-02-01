# https://leetcode.com/problems/group-anagrams/

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.


def groupAnagrams(strs):
    # make a hash table and sort each word
    groups = {}
    for word in strs:
        sorted_word = ''.join(sorted(word))
        # If the word is already a key in the dictionary, append the word to the corresponding group
        if sorted_word in groups:
            groups[sorted_word].append(word)
            # Otherwise, create a new group with the word as the key
        else:
            groups[sorted_word] = [word]
        print(groups)
    # Convert the values of the dictionary (anagram groups) to a list to get the final result
    result = list(groups.values())
    return result


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(groupAnagrams([""]))
# Output: [[""]]
print(groupAnagrams(["a"]))
# Output: [["a"]]
